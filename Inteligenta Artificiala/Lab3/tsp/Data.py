from tsp.City import City


def set_data(filename):
    """
    Transform the list of cities read from file into a list of city objects
    :param filename: the name of the file
    :return: a list of city objects and dimension
    """
    cities, dimension = read_city_data(filename)
    cities_object_list = []
    for elem in cities:
        cities_object_list.append(City(elem[0], elem[1], elem[2]))
    return cities_object_list, dimension


def read_city_data(filename):
    """
    Read cities data from file
    :param filename: the name of the file
    :return: a list of cities and dimension(the number of cities)
    """
    file = open(filename, 'r')
    # Read instance header
    name = file.readline().strip().split()[1]  # NAME
    type_ = file.readline().strip().split()[1]  # TYPE
    comment = file.readline().strip().split()[1]  # COMMENT
    dimension = int(file.readline().strip().split()[1])  # DIMENSION
    edge_weight_type = file.readline().strip().split()[1]  # EDGE_WEIGHT_TYPE
    file.readline()

    # Read node list
    cities = []
    N = int(dimension)
    for i in range(0, N):
        j, x, y = file.readline().strip().split()
        cities.append([int(j), int(x), int(y)])

    # Close input file
    file.close()

    return cities, dimension


class Data:
    """
    A class for storing the initial list of city objects and dimension
    """
    def __init__(self, filename):
        self.cities, self.dimension = set_data(filename)

    def get_city(self, index):
        return self.cities[index]

