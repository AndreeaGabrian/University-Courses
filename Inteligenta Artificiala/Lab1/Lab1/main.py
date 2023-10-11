from random_search import generate_solution, verify_solution
from get_data import read_data_from_file
from fitness_functions import fitness_ratio, fitness_sum
from steepest_hill_climbing import iterate_sch_alg
from statistics import mean


def run_random_search(iteration_number, number_of_executions):
    best_sol_from_all = 0
    avg_sol_from_all = 0
    best_list_sum = []
    avg_list_sum = []

    for j in range(number_of_executions):

        best_solution_quality_sum = 0
        best_solution_quality_ratio = 0
        avg_solution_quality_sum = 0
        avg_solution_quality_ratio = 0
        valid_iter = 0

        for i in range(iteration_number):
            objects_number, bag_max_weight, objects = read_data_from_file("rucsac-200.txt")

            best_sol_reprez_sum = []
            best_sol_reprez_ratio = []


            # -------run algorithm--------
            solution_index, binary_representation = generate_solution(objects)
            result = verify_solution(binary_representation, objects, bag_max_weight)

            # --------stats about solutions' quality-------
            quality1 = 0
            quality2 = 0

            if result[0] is True:
                valid_iter += 1
                quality1 = result[1]  # the quality for the solution with fitness=sum
                quality2 = fitness_ratio(result[1], result[2])  # the quality for the solution with fitness=ratio
                if best_solution_quality_sum < quality1:
                    best_solution_quality_sum = quality1
                    best_sol_reprez_sum = binary_representation
                if best_solution_quality_ratio < quality2:
                    best_solution_quality_ratio = quality2
                    best_sol_reprez_ratio = binary_representation
                avg_solution_quality_sum += quality1
                avg_solution_quality_ratio += quality2

        best_list_sum.append(best_solution_quality_sum)
        avg_list_sum.append(avg_solution_quality_sum / valid_iter)

    best_sol_from_all = max(best_list_sum)
    avg_sol_from_all = mean(avg_list_sum)

    return best_sol_from_all, avg_sol_from_all



            # print('Iteration:{} Valid:{} Solution:{} Weight:{}  Value:{}  Fitness_sum:{}  Fitness_ratio:{} '.format(i,
            #                                                                                                         result[
            #                                                                                                             0],
            #                                                                                                         binary_representation,
            #                                                                                                         result[
            #                                                                                                             2],
            #                                                                                                         result[
            #                                                                                                             1],
            #                                                                                                         quality1,
            #                                                                                                         quality2))

    # print("Valid solutions:{}".format(valid_iter))
    # avg_solution_quality_sum = avg_solution_quality_sum / valid_iter
    # avg_solution_quality_ratio = avg_solution_quality_ratio / valid_iter
    # print("Best solution sum(v):{}, solution: {}".format(best_solution_quality_sum, best_sol_reprez_sum))
    # print("Best solution ratio(v/w):{}, solution: {}".format(best_solution_quality_ratio, best_sol_reprez_ratio))
    # print("Avg solution sum(v):{}".format(avg_solution_quality_sum))
    # print("Avg solution ratio(v/w):{}".format(avg_solution_quality_ratio))


def run_shc(max_iter, number_of_executions):
    objects_number, bag_max_weight, objects = read_data_from_file("rucsac-200.txt")
    rez = iterate_sch_alg(objects, max_iter, bag_max_weight, number_of_executions, fitness_function=fitness_sum)
    best_sol = []
    best_sol_val = 0
    avg_sol_val = 0
    print("----------------------------------")

    for i in rez:
        print(i)
        if i[1] > best_sol_val:
            best_sol_val = i[1]
            best_sol = i[0]
        avg_sol_val += i[1]

    avg_sol_val = avg_sol_val / number_of_executions
    print("Number of executions: {}".format(number_of_executions))
    print("Number of restarting alg when stuck in local maximum: {}".format(max_iter))
    print("Best solution: {}, value: {} ".format(best_sol, best_sol_val))
    print("Avg solution value: ", avg_sol_val)


if __name__ == '__main__':
    print(run_random_search(10, 10))
    #print(run_random_search(100,10))
    #print(run_random_search(1000,10))

    #run_shc(10, 10)
    #run_shc(100, 10)
    #run_shc(1000, 10)


