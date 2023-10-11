import numpy as np


def fitness(x):
    """
    Ackley function
    :param x: point in space
    :return: function value at point x
    """
    d = len(x)
    a = 20
    b = 0.2
    c = 2 * np.pi
    value = (-a * np.exp(-b * np.sqrt(1 / d * np.sum(np.square(x))))) - (
        np.exp(1 / d * np.sum(np.cos(c * np.array(x))))) + a + np.exp(1)
    # print(value)
    return value


class Particle:
    def __init__(self, position, velocity):
        self.position = position
        self.velocity = velocity
        self.fitness = fitness(position)
        self.pbest_fitness = fitness(position)
        self.pbest_position = position

    def __str__(self):
        return "Pbest Value {} at point {}".format(self.pbest_fitness, self.pbest_position)


