from random_search import generate_solution, verify_solution
from operator import itemgetter


def max_val(l, i):
    """
    Get the maximum element of a list of lists by a specific element of the inner list
    :param l: list of lists
    :param i: i-th element of the inner list as key for max
    :return: the list index with the maximum element on the i-th position and the max value associated
    """
    return max(enumerate(sub[i] for sub in l), key=itemgetter(1))


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


def shc_alg(objects, max_iter, bag_max_weight, fitness_function):
    """
    Steepest hill climbing algorithm
    :param objects: list of objects with values and weight
    :param max_iter: number of restarting times when the alg is stuck in a local maximum
    :param bag_max_weight: bag capacity
    :param fitness_function: the fitness function by which the neighbors are evaluated
    :return: a list with all local maximum solutions for a run
    """
    results = []

    while True:
        # step 1
        # generate a valid random starting solution
        #print("iteration: ", max_iter)
        while True:
            solution_index, solution_binary = generate_solution(objects)
            rez = verify_solution(solution_binary, objects, bag_max_weight)
            if rez[0] is True:
                current_solution, current_fitness = solution_binary, fitness_function(rez[1], rez[2])
                break

        # step 2
        # get neighbors and do hill climbing
        while True:
            neighbors = get_neighbors(current_solution)
            found = False

            # verifies each neighbor and if its fitness is grater takes that point as the current solution
            # continues until it finds the neighbor with the greatest fitness
            for point in neighbors:
                rez_neighbor = verify_solution(point, objects, bag_max_weight)
                fitness_neighbor = fitness_function(rez_neighbor[1], rez_neighbor[2])

                if rez_neighbor[0] is True and fitness_neighbor > current_fitness:
                    current_solution = point
                    current_fitness = fitness_neighbor
                    found = True
                    #print("True ", current_solution, "fitness: ", current_fitness, "value: ", rez_neighbor[1])

            # if all neighbors have smaller fitness save the result and go to step 1 if the number of iteration is not 0
            if found is False:
                max_iter -= 1
                results.append([current_solution, current_fitness])
                #print("False ", current_solution, current_fitness)
                break

        if max_iter == 0:
            break

    return results


def iterate_sch_alg(objects, max_iter, bag_max_weight, number_of_executions, fitness_function):
    """
    Runs steepest hill climbing for a number of times and takes the best local maximum from each run
    :param objects: the list with object
    :param max_iter: number of restarting times when the alg is stuck in a local maximum
    :param bag_max_weight: bag's weight capacity
    :param number_of_executions: number of runs
    :param fitness_function: the fitness function by which the neighbors are evaluated
    :return: a list with the optim solution found at each run
    """
    final_results = []
    for i in range(number_of_executions):
        res = shc_alg(objects, max_iter, bag_max_weight, fitness_function)
        best_solution = res[(max_val(res, 1))[0]]
        final_results.append(best_solution)
    return final_results



