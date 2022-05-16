import numpy as np
import exercise_3


def sort_by_first_last_axis(matrix: np.ndarray) -> np.ndarray:
    """
    Sort by first and last axis
    :param matrix: Matrix to replace
    :return: Result matrix after replaced
    """
    return np.sort(np.sort(matrix, axis=0), axis=exercise_3.get_rows_cols(matrix)[1])
