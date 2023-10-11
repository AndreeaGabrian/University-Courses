from rucsac.Entity import Entity
from rucsac.Knapsack import Knapsack
import random
import numpy as np


class GeneticAlgorithm:
    def __init__(self, knapsack: Knapsack, population_number, generation_number, mutation_probability):
        self.knapsack = knapsack
        self.population_number = population_number
        self.generation_number = generation_number
        self.population = []  # list of Entity objects
        self.mutation_probability = mutation_probability

    def set_initial_population(self):
        """
        Randomly sets the initial population
        """
        for i in range(self.population_number):
            self.population.append(self.knapsack.generate_valid_solution())

    def strong_mutation(self, entity, mutation_probability):
        """
        Performs a strong mutation on a population entity on binary representation
        :param mutation_probability: the probability that mutation occurs
        :param entity: a guy from population
        :return: the modified entity
        """

        for index, bit_gene in enumerate(entity):
            q = random.uniform(0, 1)  # a random number between 0 and 1
            if q < mutation_probability:
                entity[index] = int(not bit_gene)  # flip the bit

        return entity

    def weak_mutation(self, entity, mutation_probability):
        """
        Performs a weak mutation on a population entity on binary representation
        :param mutation_probability: the probability that the mutation occurs
        :param entity: a guy from population
        :return: the modified entity
        """

        for index, bit_gene in enumerate(entity):
            q = random.uniform(0, 1)  # a random number between 0 and 1
            if q < mutation_probability:
                val = random.randint(0, 1)
                entity[index] = val

        return entity

    def single_cross_over(self, parent1, parent2):
        """
        Perform a crossover with one cut between two parents
        :param parent1: first parent
        :param parent2: second parent
        :return: two children
        """
        cut_point = random.randint(3, self.knapsack.objects_number - 3)
        child1 = [0] * self.knapsack.objects_number
        child2 = [0] * self.knapsack.objects_number

        for index, bit in enumerate(parent1):
            if index < cut_point:
                child1[index] = bit
            else:
                child2[index] = bit

        for index, bit in enumerate(parent2):
            if index < cut_point:
                child2[index] = bit
            else:
                child1[index] = bit

        return child1, child2

    def uniform_cross_over(self, parent1, parent2, prob):
        """
        Perform a uniform crossover with a probability between two parents
        :param parent1: first parent
        :param parent2: second parent
        :param prob: the probability that a gene comes from one parent or the other
        float number between 0 and 1
        :return: two children
        """

        child1 = []
        child2 = []

        for i in range(self.knapsack.objects_number):
            choice = np.random.choice([1, 2], p=[prob, 1-prob])
            if choice == 1:
                child1.append(parent1[i])
                child2.append(parent2[i])
            else:
                child1.append(parent2[i])
                child2.append(parent1[i])

        return child1, child2

    def select_parents(self):
        """
        Proportional selection. Choose the parents with a probability proportional to each entity fitness
        :return: a list with selected parents
        """
        total_fitness = sum([x.fitness for x in self.population])
        probs = [x.fitness/total_fitness for x in self.population]
        # select half population to be parents with probability distribution probs
        parents = np.random.choice(self.population, int(self.population_number/2), replace=False, p=probs)
        return parents

    def select_survivors(self):
        self.population.sort(key=lambda x: x.fitness)  # increase sort the population by fitness
        survivors = self.population[-self.population_number:]  # take the best ones to form the population for next generation
        self.population = survivors

    def genetic_algorithm1(self):
        best_solutions = []
        t = 0
        self.set_initial_population()  # initiate population
        while t < self.generation_number:
            parents = self.select_parents()   # select the parent
            random.shuffle(parents)  # shuffle the parent
            # one parent is the form [[bits],fitness]
            # set parents and get children
            for i in range(0, len(parents)-1, 2):
                # crossover the parents
                child1_rep, child2_rep = self.single_cross_over(parents[i].representation, parents[i+1].representation)
                # apply mutation to children
                child1_rep = self.strong_mutation(child1_rep, self.mutation_probability)
                child2_rep = self.strong_mutation(child2_rep, self.mutation_probability)
                # verify is children are valid, if not they are added to the population with fitness=0(penalty)
                valid, fitness, weight = self.knapsack.verify_solution(child1_rep)
                if valid:
                    self.population.append(Entity(child1_rep, fitness))
                else:
                    self.population.append(Entity(child1_rep, 0))

                valid, fitness, weight = self.knapsack.verify_solution(child2_rep)
                if valid:
                    self.population.append(Entity(child2_rep, fitness))
                else:
                    self.population.append(Entity(child2_rep, 0))

            # find the best solution from current generation
            current_best_solution = max(self.population, key=lambda x: x.fitness)
            best_solutions.append(current_best_solution)

            # select the survivors for next generation
            self.select_survivors()

            t += 1

        return best_solutions

    def genetic_algorithm2(self):
        best_solutions = []
        t = 0
        self.set_initial_population()  # initiate population
        while t < self.generation_number:
            parents = self.select_parents()   # select the parent
            random.shuffle(parents)  # shuffle the parent
            # one parent is the form [[bits],fitness]
            # set parents and get children
            for i in range(0, len(parents)-1, 2):
                # crossover the parents
                child1_rep, child2_rep = self.uniform_cross_over(parents[i].representation, parents[i+1].representation, 0.6)
                # apply mutation to children
                child1_rep = self.weak_mutation(child1_rep, self.mutation_probability)
                child2_rep = self.weak_mutation(child2_rep, self.mutation_probability)
                # verify is children are valid, if not they are added to the population with fitness=0(penalty)
                valid, fitness, weight = self.knapsack.verify_solution(child1_rep)
                if valid:
                    self.population.append(Entity(child1_rep, fitness))
                else:
                    self.population.append(Entity(child1_rep, 0))

                valid, fitness, weight = self.knapsack.verify_solution(child2_rep)
                if valid:
                    self.population.append(Entity(child2_rep, fitness))
                else:
                    self.population.append(Entity(child2_rep, 0))

            # find the best solution from current generation
            current_best_solution = max(self.population, key=lambda x: x.fitness)
            best_solutions.append(current_best_solution)

            # select the survivors for next generation
            self.select_survivors()

            t += 1

        return best_solutions







