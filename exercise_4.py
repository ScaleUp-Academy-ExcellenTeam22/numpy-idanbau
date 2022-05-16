import numpy as np


def ones_boarders_matrix(size: int) -> np.ndarray:
    """
    Get matrix with ones in the sides and zeros inside
    :param size: matrix sizeXsize dimensions
    :return: Matrix with ones in the sides and zeros inside
    """
    vector = np.ones((size, size))
    vector[1:-1, 1:-1] = 0
    return vector
