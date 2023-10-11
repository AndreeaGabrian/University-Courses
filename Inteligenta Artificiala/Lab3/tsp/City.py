import math


class City:
    def __init__(self, index, x, y):
        """
        :param index: the city index from the file
        :param x: x coordinate
        :param y: y coordinate
        """
        self.index = index
        self.x = x
        self.y = y

    def get_distance_from_city(self, other_city):
        """
        Compute the euclidian distance between two cities
        :param other_city: the city to find distance between
        :return: the distance as floating number
        """
        x_dif = self.x - other_city.x
        y_dif = self.y - other_city.y
        dist_euc_2d = math.sqrt(x_dif * x_dif + y_dif * y_dif)
        return dist_euc_2d

    def to_string(self):
        return "{} - {} - {}".format(self.index, self.x, self.y)
