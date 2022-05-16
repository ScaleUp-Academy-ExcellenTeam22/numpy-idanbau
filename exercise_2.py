import numpy as np


def create_spaced_vector(size: int, start_value: int, end_value: int) -> np.ndarray:
    return np.linspace(start_value, end_value, size)
