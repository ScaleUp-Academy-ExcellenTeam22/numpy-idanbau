import numpy as np


def combine_2_dimensional_array_show_content(first_array: np.ndarray, second_array: np.ndarray) -> None:
    """
    Combine 2 dimensional arrays and print its content
    :param first_array: First array to combine
    :param second_array: Second array to combine
    """
    for i, j in np.nditer([first_array, second_array]):
        print(f"{i}:{j}")
