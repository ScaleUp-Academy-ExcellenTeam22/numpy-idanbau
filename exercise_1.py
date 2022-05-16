import numpy as np


def create_range_vector(size: int) -> np.ndarray:
    """
    Create vector with numbers from 0 to size
    :param size: matrix size
    :return: matrix with numbers from 0 to size
    """
    return np.arange(size + 1)


def change_vector_signs_in_range(vector: np.ndarray, start_index: object, end_index: object) -> None:
    """
    Change vectors signs (minus to plus and plus to minus) in given range
    :param vector: The given vector to change signs
    :param start_index: Begin of range
    :param end_index: End of range
    """
    vector[(vector >= start_index) & (vector <= end_index)] *= -1
