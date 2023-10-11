from statistics import mean

from rucsac_tabu_search.get_data import read_data_from_file
from rucsac_tabu_search.tabu_search import tabu_search
from tsp_simulated_annealing.Data import Data
from tsp_simulated_annealing.SimulatedAnnealing import SimulatedAnnealing


def run_tabu_search():
    solutions = []
    objects_number, bag_max_weight, objects = read_data_from_file("rucsac-200.txt")
    for i in range(10):
        sol, val = tabu_search(objects, 10000, bag_max_weight, 80)
        # print(sol, val)
        solutions.append([sol, val])

    # print("---------------------------------------------")
    best = max(solutions, key=lambda item: item[1])
    worst = min(solutions, key=lambda item: item[1])
    average = mean([sol[1] for sol in solutions])
    print("Best solution: ", best)
    print("Worst solution: ", worst)
    print("Avg solution: ", average)


def run_simulated_annealing(max_iterations, T, T_min, alpha):
    data = Data("tsp_simulated_annealing/lin105.tsp")
    solutions = []
    for i in range(10):
        print(i)
        alg = SimulatedAnnealing(T, T_min, alpha, max_iterations, data.cities, data.dimension)
        solution = alg.simulated_annealing_alg2()
        solutions.append(solution)

    best = min(solutions, key=lambda item: item.distance)
    worst = max(solutions, key=lambda item: item.distance)
    average = mean([sol.distance for sol in solutions])
    print("Best distance: {} \ncities order:{}".format(best.distance, best.get_cities_order()))
    print("Worst distance: {} \ncities order:{}".format(worst.distance, worst.get_cities_order()))
    print("Average distance: ", average)


if __name__ == '__main__':
    run_simulated_annealing(10, 1000000, 0.00001, 0.9999)
    #run_tabu_search()


