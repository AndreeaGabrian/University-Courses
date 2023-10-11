from rucsac.GeneticAlgorithm import GeneticAlgorithm
from rucsac.Knapsack import Knapsack
import time
import numpy as np
import os
import random
import matplotlib.pyplot as plt

from tsp.Data import Data
from tsp.GeneticAlgorithmTSP import GeneticAlgorithmTSP
from tsp.Route import Route


def run_knapsack1(filename, population, generation, prob, var):
    parent_dir_path = r"C:\Users\gabri\Documents\AN 3 SEM 2\AI\Lab\Lab3\\rucsac"
    rucsac_file = filename.split("\\")[-1]
    dir_path = "RESULTS_file={}_alg={}_runs={}_pop={}_gen={}_mut={}".format(rucsac_file, var, 10, population, generation, prob)
    # Path
    path = os.path.join(parent_dir_path, dir_path)
    exists = os.path.exists(path)
    if not exists:
        os.mkdir(path)

    avgs = []
    bests = []
    for j in range(10):
        print(j)
        knapsack = Knapsack()
        knapsack.read_data_from_file(filename)
        alg = GeneticAlgorithm(knapsack, population, generation, prob)

        start = time.time()
        if var == 1:   # run first implementation
            solutions = alg.genetic_algorithm1()
        else:          # run second implementation
            solutions = alg.genetic_algorithm2()
        end = time.time()

        best_sol = max(solutions, key=lambda x: x.fitness)
        avg_sol = np.mean([x.fitness for x in solutions])

        avgs.append(avg_sol)
        bests.append(best_sol.fitness)

        save_filename = "alg={}_run={}_pop={}_gen={}_mut={}".format(var, j, population, generation, prob)
        file_path = os.path.join(path, save_filename)
        f = open(file_path, "w")
        f.write("Alg:{}, Run: {}, file: {}, population number: {}, generations: {}, mutation probability: {} \n".format(var, j, filename, population, generation, prob))
        for i in solutions:
            f.write(str(i.fitness) + '\n')

        f.write("Time: " + str(end - start) + " seconds \n")
        f.write("Best solution: " + str(best_sol.fitness) + " " + str(best_sol.representation) + '\n')
        f.write("Avg solution: " + str(avg_sol))
        f.close()

    save_filename2 = "SUMMARY_run={}_pop={}_gen={}_mut={}".format(10, population, generation, prob)
    file_path2 = os.path.join(path, save_filename2)
    g = open(file_path2, "w")
    g.write("SUMMARY OF {}_run={}_pop={}_gen={}_mut={} \n".format(filename, 10, population, generation, prob))
    g.write("Best solutions from all generations: \n")
    for i in bests:
        g.write(str(i) + '\n')
    g.write("Best solution over all generations: " + str(max(bests)) + '\n')
    g.write("Average solution from all generations: \n")
    for i in avgs:
        g.write(str(i) + '\n')
    g.write("Best average solution over all generations: " + str(max(avgs)) + '\n')
    g.write("Average of average solution over all generations: " + str(np.mean(avgs)) + '\n')
    g.close()


def runTSP(filename, population, generation, var):

    parent_dir_path = r"C:\Users\gabri\Documents\AN 3 SEM 2\AI\Lab\Lab3\\tsp"
    rucsac_file = filename.split("\\")[-1]
    dir_path = "RESULTS_file={}_alg={}_runs={}_pop={}_gen={}".format(rucsac_file, var, 10, population,
                                                                            generation)
    # Path
    path = os.path.join(parent_dir_path, dir_path)
    exists = os.path.exists(path)
    if not exists:
        os.mkdir(path)

    avgs = []
    bests = []

    data = Data(filename)


    for j in range(10):
        print(j)
        alg = GeneticAlgorithmTSP(data.cities, data.dimension, population, generation)

        start = time.time()
        if var == 1:  # run first implementation
            solutions = alg.generic_algorithm1()
        else:  # run second implementation
            solutions = alg.genetic_algorithm2()
        end = time.time()

        best_sol = min(solutions, key=lambda x: x.distance)
        avg_sol = np.mean([x.distance for x in solutions])

        avgs.append(avg_sol)
        bests.append(best_sol.distance)

        save_filename = "alg={}_run={}_pop={}_gen={}".format(var, j, population, generation)
        file_path = os.path.join(path, save_filename)
        f = open(file_path, "w")
        f.write(
            "Alg:{}, Run: {}, file: {}, population number: {}, generations: {} \n".format(var,
                                                                                            j,
                                                                                            filename,
                                                                                            population,
                                                                                            generation))
        for i in solutions:
            f.write(str(i.distance) + '\n')

        f.write("Time: " + str(end - start) + " seconds \n")
        f.write("Best solution: " + str(best_sol.distance) + " " + str(best_sol.get_cities_order()) + '\n')
        f.write("Avg solution: " + str(avg_sol))
        f.close()

    save_filename2 = "SUMMARY_run={}_pop={}_gen={}".format(10, population, generation)
    file_path2 = os.path.join(path, save_filename2)
    g = open(file_path2, "w")
    g.write("SUMMARY OF {}_run={}_pop={}_gen={} \n".format(filename, 10, population, generation))
    g.write("Best solutions from all generations: \n")
    for i in bests:
        g.write(str(i) + '\n')
    g.write("Best solution over all generations: " + str(min(bests)) + '\n')
    g.write("Average solution from all generations: \n")
    for i in avgs:
        g.write(str(i) + '\n')
    g.write("Best average solution over all generations: " + str(min(avgs)) + '\n')
    g.write("Average of average solution over all generations: " + str(np.mean(avgs)) + '\n')
    g.close()


if __name__ == '__main__':
    #run_knapsack1(r"C:\Users\gabri\Documents\AN 3 SEM 2\AI\Lab\Lab3\\rucsac-200.txt", 1000, 500, 0.1, 2)
    runTSP(r"C:\Users\gabri\Documents\AN 3 SEM 2\AI\Lab\Lab3\\lin105.tsp", 100, 5000, 2)






