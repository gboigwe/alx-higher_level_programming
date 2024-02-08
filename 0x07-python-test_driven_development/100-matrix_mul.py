#!/usr/bin/python3
"""Matrix multiplication function."""

def matrix_mul(m_a, m_b):
    """Multiplies two matrices.

    Args:
        m_a (list): The first matrix.
        m_b (list): The second matrix.

    Returns:
        list: The result of the multiplication, or None if matrices are invalid.

    Raises:
        TypeError: If either matrix is not a list of lists.
        ValueError: If either matrix is empty, has rows of different sizes, or
             the inner dimensions are incompatible for multiplication.
    """

    if not isinstance(m_a, list) or not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")

    if not isinstance(m_b, list) or not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if not m_a:
        raise ValueError("m_a cannot be empty")

    if not m_b:
        raise ValueError("m_b cannot be empty")

    m_a_cols = len(m_a[0])
    if any(len(row) != m_a_cols for row in m_a):
        raise ValueError("Rows of m_a must have the same size")

    m_b_rows = len(m_b)
    if any(len(row) != m_a_cols for row in m_b):
        raise ValueError("Rows of m_b must have the same size")

    if m_a_cols != len(m_b):
        raise ValueError("Incompatible inner dimensions for multiplication")

    result = []
    for i in range(len(m_a)):
        row = []
        for j in range(len(m_b[0])):
            num = 0
            for k in range(m_a_cols):
                num += m_a[i][k] * m_b[k][j]
            row.append(num)
        result.append(row)

    return result
