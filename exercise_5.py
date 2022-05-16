import numpy as np
import exercise_3


def append_vector_to_each_row(matrix: np.ndarray, vector: np.ndarray) -> np.ndarray:
    """
    :param matrix: Matrix to add vectors in it
    :param vector: Vector to add to each matrix row
    :return: New matrix with vector appended to each row
    """
    matrix_rows, matrix_cols = exercise_3.get_rows_cols(matrix)
    if matrix_cols != vector.size:
        raise Exception("Invalid vector size")
    result = np.empty_like(matrix)
    for row in range(matrix_rows):
        result[row, :] = matrix[row, :] + vector
    return result
