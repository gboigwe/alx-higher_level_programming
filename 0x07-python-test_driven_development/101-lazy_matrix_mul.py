#!/usr/bin/python3
"""
Module function that multiplies 2 matrices
"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """ Function that multiplies 2 matrices

    Args:
        m_a: a matrix
        m_b: b matrix

    Returns:
        the multiplication

    """

    return (np.matmul(m_a, m_b))
