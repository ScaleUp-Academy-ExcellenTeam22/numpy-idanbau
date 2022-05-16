import numpy as np


def create_matrix_with_ones_diagonal(array_size: int) -> np.ndarray:
    """
    Matrix with 1 in all diagonals
    :param array_size: Array size to have 1 on them
    :return: matrix with 1's in its diagonals
    """
    return np.eye(array_size)
