import numpy as np

from rucsac_tabu_search.fitness_functions import fitness_sum


def verify_solution(binary_solution, object_list, max_weight):
    """
    Verifies is a solution is valid. A Solution is valid if the total objects weight is less that the bag capacity
    :param binary_solution: the binary representation of the solution(list of bits)
    :param object_list: the list with object value and weight
    :param max_weight: the bag max weight
    :return: True is the solution is valid, False otherwise and the total weight and value put in the bag
    """
    solution_weight = [bit * obj[1] for bit, obj in zip(binary_solution, object_list)]
    solution_value = [bit * obj[0] for bit, obj in zip(binary_solution, object_list)]

    rez_w = sum(solution_weight)
    rez_v = sum(solution_value)

    if rez_w <= max_weight:
        return True, rez_v, rez_w
    return False, rez_v, rez_w


def generate_solution(objects):
    """
    Generate a random binary solution
    :param objects: list of the form [(value, weight)]
    :return: a possible solution in real representation(solution_index) and a binary representation
    """

    solution_index = []
    binary_representation = []
    for index, (o_value, o_weight) in enumerate(objects):
        choose_obj = np.random.choice([0, 1])
        if choose_obj == 1:
            solution_index.append(index)
        binary_representation.append(choose_obj)

    return solution_index, binary_representation


def get_neighbors(binary_solution):
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


def get_neighbors_bit_index(binary_solution):
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


def update_memory(memory):
    for index, elem in enumerate(memory):
        if elem > 0:
            memory[index] = elem - 1


def tabu_search(objects, max_iter, bag_max_weight, tabu_number, fitness_function=fitness_sum):
    best_solution = ""
    best_fitness = 0
    memory = [0] * len(objects)

    # step 1
    # generate a valid random solution
    while True:
        solution_index, solution_binary = generate_solution(objects)
        rez = verify_solution(solution_binary, objects, bag_max_weight)
        if rez[0] is True:
            current_solution, current_fitness = solution_binary, fitness_function(rez[1], rez[2])
            break

    best_solution = current_solution
    best_fitness = current_fitness

    while max_iter != 0:
        # update memory
        update_memory(memory)

        # step 2
        # get neighbors
        neighbors = get_neighbors_bit_index(current_solution)

        memory_index_to_update = 0

        max_neighbour_non_tabu_sol = ""
        max_neighbour_non_tabu_fitness = 0
        for (point, index) in neighbors:
            rez_neighbor = verify_solution(point, objects, bag_max_weight)
            fitness_neighbor = fitness_function(rez_neighbor[1], rez_neighbor[2])

            # from neighborhood solutions, get the best candidate that is not on the Tabu List(memory list)
            if rez_neighbor[0] is True and fitness_neighbor > max_neighbour_non_tabu_fitness and memory[index] == 0:
                max_neighbour_non_tabu_sol = point
                max_neighbour_non_tabu_fitness = fitness_neighbor
                memory_index_to_update = index

        if max_neighbour_non_tabu_fitness > best_fitness:
            best_solution = max_neighbour_non_tabu_sol
            best_fitness = max_neighbour_non_tabu_fitness

        current_solution = max_neighbour_non_tabu_sol
        current_fitness = max_neighbour_non_tabu_fitness

        # update the memory list with the best candidate solution in this iteration
        memory[memory_index_to_update] = tabu_number

        max_iter -= 1

    return best_solution, best_fitness


