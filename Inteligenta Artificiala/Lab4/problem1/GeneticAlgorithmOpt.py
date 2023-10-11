import random

import numpy as np

from problem1.Solution import Solution


class GeneticAlgorithm:
    def __init__(self, function, population_number, generation_number, mutation_probability, crossover_probability, bounds, dimension):
        self.function = function  # function to optimize
        self.population_number = population_number
        self.generation_number = generation_number
        self.population = []  # list of Solution objects
        self.mutation_probability = mutation_probability
        self.crossover_probability = crossover_probability
        self.bounds = bounds  # list with lower and upper bound for function domain
        self.dimension = dimension

    def set_initial_population(self):
        """
        Generates random solutions for initial population
        :return: the initial population
        """
        for i in range(self.population_number):
            point = np.random.uniform(low=self.bounds[0], high=self.bounds[1], size=self.dimension)

            self.population.append(Solution(point))

    def discrete_crossover(self, parent1, parent2):
        """
        Performs a discrete crossover. For each position i for the first child selects with crossover_probability
        the parent from which the gene at the position i is chosen. For the other child, the gene is taken from the
        other parent at position i.
        :param parent1: first parent
        :param parent2: other parent
        :return: two children
        """
        child1 = []
        child2 = []
        for i in range(self.dimension):
            choice = np.random.choice([1, 2], 1, p=[self.crossover_probability, 1-self.crossover_probability])
            if choice == 1:
                child1.append(parent1[i])
                child2.append(parent2[i])
            else:
                child1.append(parent2[i])
                child2.append(parent1[i])
        return child1, child2

    def unique_convex_crossover(self, parent1, parent2):
        """
        Performs a unique convex crossover. Randomly selects a gene position. Both children will have
        this gene changed by a formula and the other genes will remain as in parents
        :param parent1: first parent
        :param parent2: other parent
        :return: two children
        """
        gene_index = random.randint(0, self.dimension-1)
        alpha = random.uniform(0, 1)  # alpha is chosen for every pair of parents
        new_gene = alpha * parent2[gene_index] + (1-alpha) * parent1[gene_index]
        child1 = parent1.copy()
        child2 = parent2.copy()
        child1[gene_index] = new_gene
        child2[gene_index] = new_gene
        return child1, child2

    def uniform_mutation(self, child):
        """
        Performs a uniform mutation on given child. Every gene can suffer a mutation
        with mutation_probability and be changed with a random generated real number between bounds
        :param child: child to mutate
        :return: mutated child
        """
        for index, gene in enumerate(child):
            q = random.uniform(0, 1)  # a random number between bounds
            if q < self.mutation_probability:
                new_gene = random.uniform(self.bounds[0], self.bounds[1])
                child[index] = int(new_gene)  # change the gene
        return child

    def select_parents(self):
        """
        Proportional selection. Choose the parents with a probability proportional to each solution fitness
        :return: a list with selected parents
        """
        fitnesses = [1/x.fitness for x in self.population]
        # total_fitness = sum([1/x.fitness for x in self.population])
        total_fitness = sum(fitnesses)
        # probs = [x.fitness/total_fitness for x in self.population]
        probs = [x/total_fitness for x in fitnesses]
        # select 50% from population to be parents with probability distribution probs
        fit_parents = np.random.choice(self.population, int(self.population_number/2), replace=False, p=probs)

        return fit_parents

    def select_survivors(self):
        """
        Selects survivors for next generation based on personal fitness. The parents are chosen with a uniform probability
        distribution based on fitness
        :return: selected parents
        """
        self.population.sort(key=lambda x: x.fitness)  # increase sort the population by fitness
        survivors = self.population[:self.population_number]  # take the best ones to form the population for next generation
        # best fitness hear means small values
        self.population = survivors

    def genetic_algorithm1(self):
        best_solutions = []
        avg_solutions = []
        t = 0
        self.set_initial_population()  # initiate population
        while t < self.generation_number:
            parents = self.select_parents()  # select the parent
            random.shuffle(parents)  # shuffle the parent
            # one parent is the form [point,fitness]
            # set parents and get children
            for i in range(0, len(parents) - 1, 2):
                # crossover the parents
                child1_point, child2_point = self.discrete_crossover(parents[i].point, parents[i + 1].point)
                # apply mutation to children
                child1_point = self.uniform_mutation(child1_point)
                child2_point = self.uniform_mutation(child2_point)
                # create children solution objects and add them to the population
                self.population.append(Solution(child1_point))
                self.population.append(Solution(child2_point))

            # find the best solution from current generation
            current_best_solution = min(self.population, key=lambda x: x.fitness)
            best_solutions.append(current_best_solution)

            # find the average solution from current population
            current_avg = np.mean([x.fitness for x in self.population])
            avg_solutions.append(current_avg)

            # select the survivors for next generation
            self.select_survivors()

            t += 1

        return best_solutions, avg_solutions

    def genetic_algorithm2(self):
        best_solutions = []
        avg_solutions = []
        t = 0
        self.set_initial_population()  # initiate population
        while t < self.generation_number:
            parents = self.select_parents()   # select the parent
            random.shuffle(parents)  # shuffle the parent
            # one parent is the form [point,fitness]
            # set parents and get children
            for i in range(0, len(parents)-1, 2):
                # crossover the parents
                child1_point, child2_point = self.unique_convex_crossover(parents[i].point, parents[i+1].point)
                # apply mutation to children
                child1_point = self.uniform_mutation(child1_point)
                child2_point = self.uniform_mutation(child2_point)
                # create children solution objects and add them to the population
                self.population.append(Solution(child1_point))
                self.population.append(Solution(child2_point))

            # find the best solution from current generation
            current_best_solution = min(self.population, key=lambda x: x.fitness)
            best_solutions.append(current_best_solution)

            # find the average solution from current population
            current_avg = np.mean([x.fitness for x in self.population])
            avg_solutions.append(current_avg)

            # select the survivors for next generation
            self.select_survivors()

            t += 1

        return best_solutions, avg_solutions
