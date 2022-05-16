import numpy as np
import matplotlib.pyplot as plt


def compute_x_y_points_on_sine_curve(start, end, step, d_type: type)->None:
    """
    Show graph of x parameters and x sin value
    :param start: Start sequence
    :param end: end sequence
    :param step: step between cells in sequence
    :param d_type: type of the values
    """
    # Compute the x and y coordinates for points on a sine curve
    x_coordinates_range = np.arange(start, end, step, d_type)
    sin_of_x_coordinates_range = np.sin(x_coordinates_range)
    plt.plot(x_coordinates_range, sin_of_x_coordinates_range)
    plt.show()
