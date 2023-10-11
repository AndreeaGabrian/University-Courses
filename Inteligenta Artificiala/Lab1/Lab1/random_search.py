import numpy as np


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





