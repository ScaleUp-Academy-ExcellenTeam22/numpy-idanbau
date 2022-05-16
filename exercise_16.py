import numpy as np


def sort_by_student_id_height(student_id_array: np.array, student_height_array: np.array) -> np.array:
    return np.lexsort((student_id_array, student_height_array))
