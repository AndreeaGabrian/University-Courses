import random


class Route:
    """
    A class for representing a possible solution of tsp, meaning a valid configuration of all cities
    """

    def __init__(self, dimension, cities):
        self.dimension = dimension
        self.cities = cities
        self.distance = self.get_route_distance()

    def get_random_route(self):
        """
        Generate a random route/configuration of cities
        :return: a Route object with random cities order
        """
        cities_copy = self.cities.copy()
        random.shuffle(cities_copy)
        return Route(self.dimension, cities_copy)

    def swap_2_cities(self):
        """
        Swap two random cities from the list
        :return: a Route object with two random cities swapped
        """
        index1 = random.randint(1, 105)
        index2 = random.randint(1, 105)
        city1_route_index = [self.cities.index(city) for city in self.cities if city.index == index1][0]
        city2_route_index = [self.cities.index(city) for city in self.cities if city.index == index2][0]
        new_cities_order = self.cities.copy()
        city1 = new_cities_order[city1_route_index]
        city2 = new_cities_order[city2_route_index]
        new_cities_order[city1_route_index] = city2
        new_cities_order[city2_route_index] = city1

        return Route(self.dimension, new_cities_order)

    def get_route_distance(self):
        """
        Computes the overall distance of a route, starting from the first city in the list and ending into it
        :return: the total distance of the route
        """
        distance = 0
        for i in range(self.dimension-1):
            distance += self.cities[i].get_distance_from_city(self.cities[i+1])
        distance += self.cities[-1].get_distance_from_city(self.cities[0])  # add the distance between last and first city to close the loop

        return distance

    def get_cities_order(self):
        """
        Get the cities indexes from the route
        :return: a list with cities indexes in the crossing order
        """
        return [city.index for city in self.cities]

