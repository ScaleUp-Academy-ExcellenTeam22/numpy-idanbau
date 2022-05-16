import numpy as np


def rand_matrix(size: int) -> np.ndarray:
    """
    get rand x*x matrix
    :param size: size of matrix
    :return: x*x matrix with random values
    """
    return np.arange(size * size, dtype='int').reshape(-1, size)


def swap_first_last_rows(matrix: np.ndarray) -> np.ndarray:
    """
    Swap between first and last rows
    :param matrix: Matrix to replace rows in
    :return: New matrix with replace rows
    """
    return matrix[::-1]
