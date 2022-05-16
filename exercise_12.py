import numpy as np


def remove_single_dimensional_entries(matrix: np.ndarray) -> np.ndarray:
    """
    Remove signal dimensional from the matrix
    :param matrix: Input matrix to execute
    :return: Matrix with removed diagonal on it
    """
    return np.squeeze(matrix)
