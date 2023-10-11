import time
import numpy as np
from problem1.GeneticAlgorithmOpt import GeneticAlgorithm
from problem1.function import optimize_function
import os
import matplotlib.pyplot as plt

from problem2.pso import PSO


def run_pb_1_alg1(population, generations, mut_prob, cros_prob, dim):
    parent_dir_path = r"C:\Users\gabri\Documents\AN 3 SEM 2\AI\Lab\Lab4\\problem1"
    alg = GeneticAlgorithm(optimize_function, population, generations, mut_prob, cros_prob, [-32.768, 32.768], dim)

    file_path = "RESULTS_alg=1_runs={}_pop={}_gen={}_mut={}_cross={}_dim{}".format(10, alg.population_number,
                                                                                   alg.generation_number,
                                                                                   alg.mutation_probability,
                                                                                   alg.crossover_probability,
                                                                                   alg.dimension)
    # Path
    save_path = os.path.join(parent_dir_path, file_path)

    avgs = []
    bests = []

    start = time.time()

    for i in range(10):
        solutions_best, solutions_avg = alg.genetic_algorithm1()
        best_sol = min(solutions_best, key=lambda x: x.fitness)
        avg_sol = min(solutions_avg)
        bests.append(best_sol)
        avgs.append(avg_sol)

        best_solutions_plot = [z.fitness for z in solutions_best]

        # plot solution's evolution
        if i == 0:
            plot_sol(i + 1, 1, best_solutions_plot, solutions_avg, alg.generation_number, alg.population_number,
                     alg.dimension)

    end = time.time()

    f = open(save_path, "w")
    f.write("Best solutions from all runs: \n")
    for i in bests:
        f.write(str(i.fitness) + '\n')

    f.write("Best solutions overall runs: \n")
    f.write(str(min(bests, key=lambda x: x.fitness)) + '\n')
    f.write("Average solution from all runs: \n")
    for i in avgs:
        f.write(str(i) + '\n')
    f.write("Best average solution over all generations: " + str(min(avgs)) + '\n')
    f.write("Time: " + str(end - start) + " seconds \n")
    f.close()


def plot_sol(run, alg, best, avg, generations, pop_number, dim):
    x = [j for j in range(1, generations + 1)]
    plt.plot(x, best, label="Best")
    optim = [0] * generations
    plt.plot(x, avg, label="Average")
    plt.plot(x, optim, label="Optimal")

    plt.xlabel("Generation")
    plt.ylabel("Fitness")

    plt.title("run{}_alg{}_dim{}_pop{}_Generations{}.png".format(run, alg, dim, pop_number, generations))
    plt.legend()

    plt.savefig("run{}_alg{}_dim{}_pop{}_Generations{}.png".format(run, alg, dim, pop_number, generations))
    # plt.show()
    plt.clf()  # clear the current figure


def plot_sol_pso(run, best, iterations, pop_number, dim):
    x = [j for j in range(1, len(best)+1)]
    plt.plot(x, best, '-o', label="Best")
    optim = [0] * len(best)
    plt.plot(x, optim, label="Optimal")

    plt.xlabel("iterations")
    plt.ylabel("Fitness")

    plt.title("run{}_pso_dim{}_pop{}iterations{}.png".format(run, dim, pop_number, iterations))
    plt.legend()

    plt.savefig("run{}_pso_dim{}_pop{}iterations{}.png".format(run, dim, pop_number, iterations))
    # plt.show()
    plt.clf()  # clear the current figure


def run_pb_1_alg2(population, generations, mut_prob, cros_prob, dim):
    parent_dir_path = r"C:\Users\gabri\Documents\AN 3 SEM 2\AI\Lab\Lab4\\problem1"
    alg = GeneticAlgorithm(optimize_function, population, generations, mut_prob, cros_prob, [-32.768, 32.768], dim)

    file_path = "RESULTS_alg=2_runs={}_pop={}_gen={}_mut={}_cross={}_dim={}".format(10, alg.population_number,
                                                                                    alg.generation_number,
                                                                                    alg.mutation_probability,
                                                                                    alg.crossover_probability,
                                                                                    alg.dimension)
    # Path
    save_path = os.path.join(parent_dir_path, file_path)

    avgs = []
    bests = []

    start = time.time()

    for i in range(10):
        solutions_best, solutions_avg = alg.genetic_algorithm2()
        best_sol = min(solutions_best, key=lambda x: x.fitness)
        avg_sol = min(solutions_avg)
        bests.append(best_sol)
        avgs.append(avg_sol)

        best_solutions_plot = [z.fitness for z in solutions_best]

        # plot solution's evolution
        if i == 0:
            plot_sol(i + 1, 2, best_solutions_plot, solutions_avg, alg.generation_number, alg.population_number,
                     alg.dimension)

    end = time.time()

    f = open(save_path, "w")
    f.write("Best solutions from all runs: \n")
    for i in bests:
        f.write(str(i) + '\n')

    f.write("Best solutions overall runs: \n")
    f.write(str(min(bests, key=lambda x: x.fitness)) + '\n')
    f.write("Average solution from all runs: \n")
    for i in avgs:
        f.write(str(i) + '\n')
    f.write("Best average solution over all generations: " + str(min(avgs)) + '\n')
    f.write("Time: " + str(end - start) + " seconds \n")
    f.close()


def run_pso(population_number, iteration_number, dimension):
    parent_dir_path = r"C:\Users\gabri\Documents\AN 3 SEM 2\AI\Lab\Lab4\\problem2"
    pso = PSO(population_number, iteration_number, [-32.768, 32.768], dimension)


    file_path = "pso_results_runs={}_pop={}_iter={}_dim={}".format(10, pso.population_number,
                                                                     pso.iteration_number,
                                                                     pso.dimension)
    # Path
    save_path = os.path.join(parent_dir_path, file_path)

    avgs = []
    bests = []

    start = time.time()

    for i in range(10):
        solutions_best = pso.pso_alg(c1=2.0, c2=2.0, w=1.0, vmax=50)
        best_sol = min(solutions_best, key=lambda x: x.pbest_fitness)
        avg_sol = np.mean([x.pbest_fitness for x in solutions_best])
        bests.append(best_sol)
        avgs.append(avg_sol)

        best_solutions_plot = [z.pbest_fitness for z in solutions_best]

        # plot solution's evolution
        if i == 0:
            plot_sol_pso(i + 1, best_solutions_plot, pso.iteration_number, pso.population_number,
                     pso.dimension)

    end = time.time()

    f = open(save_path, "w")
    f.write("Best solutions from all runs: \n")
    for i in bests:
        f.write(str(i) + '\n')

    f.write("Best solutions overall runs: \n")
    f.write(str(min(bests, key=lambda x: x.pbest_fitness)) + '\n')
    f.write("Average best solution from all runs: \n")
    for i in avgs:
        f.write(str(i) + '\n')
    f.write("Best average best solution over all generations: " + str(min(avgs)) + '\n')
    f.write("Time: " + str(end - start) + " seconds \n")
    f.close()


if __name__ == '__main__':
    # alg 1 run -----------------------------------------------------------------
    # run_pb_1_alg1(population=10, generations=10, mut_prob=0.4, cros_prob=0.3, dim=2)
    # run_pb_1_alg1(population=10, generations=20, mut_prob=0.4, cros_prob=0.3, dim=2)
    # run_pb_1_alg1(population=100, generations=20, mut_prob=0.4, cros_prob=0.3, dim=2)
    # run_pb_1_alg1(population=100, generations=100, mut_prob=0.4, cros_prob=0.3, dim=2)
    # run_pb_1_alg1(population=100, generations=200, mut_prob=0.4, cros_prob=0.3, dim=2)
    #
    # run_pb_1_alg1(population=10, generations=10, mut_prob=0.4, cros_prob=0.3, dim=8)
    # run_pb_1_alg1(population=10, generations=20, mut_prob=0.4, cros_prob=0.3, dim=8)
    # run_pb_1_alg1(population=100, generations=20, mut_prob=0.4, cros_prob=0.3, dim=8)
    # run_pb_1_alg1(population=100, generations=100, mut_prob=0.4, cros_prob=0.3, dim=8)
    # run_pb_1_alg1(population=100, generations=200, mut_prob=0.4, cros_prob=0.3, dim=8)

    run_pb_1_alg1(population=200, generations=200, mut_prob=0.4, cros_prob=0.3, dim=8)
    run_pb_1_alg1(population=200, generations=400, mut_prob=0.4, cros_prob=0.3, dim=8)
    run_pb_1_alg1(population=200, generations=500, mut_prob=0.4, cros_prob=0.3, dim=8)

    # run_pb_1_alg1(population=10, generations=10, mut_prob=0.4, cros_prob=0.3, dim=16)
    # run_pb_1_alg1(population=10, generations=20, mut_prob=0.4, cros_prob=0.3, dim=16)
    # run_pb_1_alg1(population=100, generations=20, mut_prob=0.4, cros_prob=0.3, dim=16)
    # run_pb_1_alg1(population=100, generations=100, mut_prob=0.4, cros_prob=0.3, dim=16)
    # run_pb_1_alg1(population=100, generations=200, mut_prob=0.4, cros_prob=0.3, dim=16)

    run_pb_1_alg1(population=200, generations=200, mut_prob=0.4, cros_prob=0.3, dim=16)
    run_pb_1_alg1(population=200, generations=400, mut_prob=0.4, cros_prob=0.3, dim=16)
    run_pb_1_alg1(population=200, generations=500, mut_prob=0.4, cros_prob=0.3, dim=16)

    print("Done alg1")

    # run alg 2--------------------------------------------------------------------------
    # run_pb_1_alg2(population=10, generations=10, mut_prob=0.4, cros_prob=0.3, dim=2)
    # run_pb_1_alg2(population=10, generations=20, mut_prob=0.4, cros_prob=0.3, dim=2)
    # run_pb_1_alg2(population=100, generations=20, mut_prob=0.4, cros_prob=0.3, dim=2)
    # run_pb_1_alg2(population=100, generations=100, mut_prob=0.4, cros_prob=0.3, dim=2)
    # run_pb_1_alg2(population=100, generations=200, mut_prob=0.4, cros_prob=0.3, dim=2)
    #
    # run_pb_1_alg2(population=10, generations=10, mut_prob=0.4, cros_prob=0.3, dim=8)
    # run_pb_1_alg2(population=10, generations=20, mut_prob=0.4, cros_prob=0.3, dim=8)
    # run_pb_1_alg2(population=100, generations=20, mut_prob=0.4, cros_prob=0.3, dim=8)
    # run_pb_1_alg2(population=100, generations=100, mut_prob=0.4, cros_prob=0.3, dim=8)
    # run_pb_1_alg2(population=100, generations=200, mut_prob=0.4, cros_prob=0.3, dim=8)

    run_pb_1_alg2(population=200, generations=200, mut_prob=0.4, cros_prob=0.3, dim=8)
    run_pb_1_alg2(population=200, generations=400, mut_prob=0.4, cros_prob=0.3, dim=8)
    run_pb_1_alg2(population=200, generations=500, mut_prob=0.4, cros_prob=0.3, dim=8)

    # run_pb_1_alg2(population=10, generations=10, mut_prob=0.4, cros_prob=0.3, dim=16)
    # run_pb_1_alg2(population=10, generations=20, mut_prob=0.4, cros_prob=0.3, dim=16)
    # run_pb_1_alg2(population=100, generations=20, mut_prob=0.4, cros_prob=0.3, dim=16)
    # run_pb_1_alg2(population=100, generations=100, mut_prob=0.4, cros_prob=0.3, dim=16)
    # run_pb_1_alg2(population=100, generations=200, mut_prob=0.4, cros_prob=0.3, dim=16)

    run_pb_1_alg2(population=200, generations=200, mut_prob=0.4, cros_prob=0.3, dim=16)
    run_pb_1_alg2(population=200, generations=400, mut_prob=0.4, cros_prob=0.3, dim=16)
    run_pb_1_alg2(population=200, generations=500, mut_prob=0.4, cros_prob=0.3, dim=16)
    print("Done alg2")

    # run pso
    # run_pso(population_number=20, iteration_number=100, dimension=2)
    # run_pso(population_number=80, iteration_number=100, dimension=2)
    # run_pso(population_number=100, iteration_number=100, dimension=2)
    # run_pso(population_number=100, iteration_number=200, dimension=2)
    # run_pso(population_number=100, iteration_number=400, dimension=2)
    #
    # run_pso(population_number=20, iteration_number=100, dimension=8)
    # run_pso(population_number=80, iteration_number=100, dimension=8)
    # run_pso(population_number=100, iteration_number=100, dimension=8)
    # run_pso(population_number=100, iteration_number=200, dimension=8)
    # run_pso(population_number=100, iteration_number=400, dimension=8)
    #
    # run_pso(population_number=20, iteration_number=100, dimension=16)
    # run_pso(population_number=80, iteration_number=100, dimension=16)
    # run_pso(population_number=100, iteration_number=100, dimension=16)
    # run_pso(population_number=100, iteration_number=200, dimension=16)
    # run_pso(population_number=100, iteration_number=400, dimension=16)
    print("Done pso")
