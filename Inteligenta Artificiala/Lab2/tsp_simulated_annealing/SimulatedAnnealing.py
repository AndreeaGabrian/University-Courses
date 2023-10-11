import math
import random

from tsp_simulated_annealing.Route import Route
from random import uniform


class SimulatedAnnealing:
    """
    Class for simulated annealing algorithm
    """
    def __init__(self, temperature, min_temperature, alpha, max_iterations, cities, dimension):
        self.temperature = temperature
        self.min_temperature = min_temperature
        self.alpha = alpha
        self.max_iterations = max_iterations
        self.cities = cities
        self.dimension = dimension

    def simulated_annealing_alg(self):
        current_route = Route(self.dimension, self.cities).get_random_route()  # starts with a random route
        while self.temperature > self.min_temperature:
            iterations = self.max_iterations
            while iterations > 0:  # while there are iterations left
                neighbor_route = current_route.swap_2_cities()  # generate a neighbor by swapping two cities
                delta = neighbor_route.get_route_distance() - current_route.get_route_distance()
                if delta < 0:  # if the neighbor route is shorter move into it
                    current_route = neighbor_route
                elif random.uniform(0, 1) < math.exp(-delta/self.temperature):  # if the neighbour route is worst it can be choosen by
                                                                                # a probability conditioned by distance and temperature
                    current_route = neighbor_route
                iterations -= 1

            self.temperature = self.alpha * self.temperature  # decrease the temperatures

        return current_route

    def simulated_annealing_alg2(self):
        current_route = Route(self.dimension, self.cities).get_random_route()  # starts with a random route
        iterations = self.max_iterations
        while iterations > 0: # while there are iterations left
            while self.temperature > self.min_temperature:
                neighbor_route = current_route.swap_2_cities()  # generate a neighbor by swapping two cities
                delta = neighbor_route.get_route_distance() - current_route.get_route_distance()
                if delta < 0:  # if the neighbor route is shorter move into it
                    current_route = neighbor_route
                elif random.uniform(0, 1) < math.exp(-delta/self.temperature):  # if the neighbour route is worst it can be choosen by
                                                                                # a probability conditioned by distance and temperature
                    current_route = neighbor_route

                self.temperature = self.alpha * self.temperature  # decrease the temperature
            iterations -= 1

        return current_route

