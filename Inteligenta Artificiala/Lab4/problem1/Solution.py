from problem1.function import optimize_function


class Solution:
    def __init__(self, point):
        self.point = point  # list or np array
        self.fitness = optimize_function(point)

    def __str__(self):
        return "Value: {} at point: {}".format(self.fitness, self.point)
