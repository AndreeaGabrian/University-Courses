import numpy as np

from rucsac.Entity import Entity


class Knapsack:
    def __init__(self):
        self.objects_number = 0
        self.bag_max_weight = 0
        self.objects = None

    def read_data_from_file(self, filename):
        objects = []
        with open(filename) as file:
            count = 0
            for line in file:
                count += 1
                line = line.strip()
                line = line.split(" ")
                line = [elem for elem in line if elem != ""]
                if count == 1:
                    objects_number = int(line[0])
                elif count != 1 and len(line) == 1:
                    bag_max_weight = int(line[0])
                else:
                    objects.append((int(line[1]), int(line[2])))

        self.objects_number = objects_number
        self.objects = objects
        self.bag_max_weight = bag_max_weight

    def fitness_sum(self, value, weight=0):
        return value

    def generate_solution(self):
        """
        Generate a random binary solution
        :return: a possible solution in real representation(solution_index) and a binary representation
        """
        binary_representation = []
        for index, (o_value, o_weight) in enumerate(self.objects):
            choose_obj = np.random.choice([0, 1])
            binary_representation.append(choose_obj)
        return binary_representation

    def verify_solution(self, binary_solution):
        """
        Verifies is a solution is valid. A Solution is valid if the total objects weight is less that the bag capacity
        :param binary_solution: the binary representation of the solution(list of bits)
        :return: True is the solution is valid, False otherwise and the total weight and value put in the bag
        """
        solution_weight = [bit * obj[1] for bit, obj in zip(binary_solution, self.objects)]
        solution_value = [bit * obj[0] for bit, obj in zip(binary_solution, self.objects)]

        rez_w = sum(solution_weight)
        rez_v = sum(solution_value)

        if rez_w <= self.bag_max_weight:
            return True, rez_v, rez_w
        return False, rez_v, rez_w

    def get_neighbors(self, binary_solution):
        """
        Compute the neighbors of a solution by flipping a bit at a time
        :param binary_solution: a valid solution
        :return: the list with the neighbors
        """
        neighbors = []
        for index, bit in enumerate(binary_solution):
            neighbor = binary_solution.copy()
            if bit == 0:
                neighbor[index] = 1
            else:
                neighbor[index] = 0
            neighbors.append(neighbor)
        return neighbors

    def get_neighbors_bit_index(self, binary_solution):
        """
        Compute the neighbors of a solution by flipping a bit at a time
        :param binary_solution: a valid solution
        :return: the list with the neighbors and the flipped bit index
        """
        neighbors = []
        for index, bit in enumerate(binary_solution):
            neighbor = binary_solution.copy()
            if bit == 0:
                neighbor[index] = 1
            else:
                neighbor[index] = 0
            neighbors.append((neighbor, index))
        return neighbors

    def generate_valid_solution(self):
        while True:
            solution_binary = self.generate_solution()
            rez = self.verify_solution(solution_binary)
            if rez[0] is True:
                solution, fitness = solution_binary, self.fitness_sum(rez[1], rez[2])
                break
        return Entity(solution, fitness)