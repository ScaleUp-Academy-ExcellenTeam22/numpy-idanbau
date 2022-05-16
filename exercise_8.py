import numpy as np


def replace_numbers(matrix: np.ndarray, new_value, equal_number, less_number, greater_number) -> np.ndarray:
    """
    Replace numbers in matrix
    :param new_value:
    :param matrix: matrix to replace values
    :param equal_number: equal numbers to replace in the matrix
    :param less_number: less comparison numbers in the matrix to replace
    :param greater_number: great comparisons numbers to replace
    :return: matrix with replaced numbers
    """
    np.where(matrix == equal_number, new_value, matrix)
    np.where(matrix < less_number, new_value, matrix)
    np.where(matrix > greater_number, new_value, matrix)
