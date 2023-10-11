import numpy as np


def optimize_function(x):
    """
    Ackley function
    :param x: point in space
    :return: function value at point x
    """
    d = len(x)
    a = 20
    b = 0.2
    c = 2 * np.pi
    value = (-a * np.exp(-b * np.sqrt(1/d * np.sum(np.square(x)))) ) - ( np.exp(1/d * np.sum(np.cos(c*np.array(x)))) ) + a + np.exp(1)
    # print(value)
    return value
