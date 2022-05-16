import numpy as np


def combine_2_vectors(first_vector: np.ndarray, second_vector: np.ndarray) -> np.ndarray:
    """
    Combine 2 vectors together
    :param first_vector: Input first vector to combine
    :param second_vector: Input second vector to combine
    :return: Combined vector
    """
    return np.dstack(first_vector, second_vector)
