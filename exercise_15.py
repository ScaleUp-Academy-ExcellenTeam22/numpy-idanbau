import numpy as np


def three_dimension_matrix_random_variables() -> np.ndarray:
    """
    Create 3 dimensional matrix with size of 300,400,5 with random values
    :return: 3 dimensional matrix with size of 300,400,5 with random values
    """
    np.random.seed(32)
    return np.random.randint(low=0, high=256, size=(300, 400, 5), dtype=np.uint8)
