from tsp.Route import Route
import numpy as np
import random


class GeneticAlgorithmTSP:
    def __init__(self, cities, dimension, population_number, generation_number):
        self.cities = cities  # list of City objects
        self.dimension = dimension
        self.population_number = population_number
        self.generation_number = generation_number
        self.population = []  # list of Route objects

    def set_initial_population(self):
        """
        Randomly sets the initial population
        """
        route = Route(self.dimension, self.cities)
        for i in range(self.population_number):
            self.population.append(route.get_random_route())

    def select_parents(self):
        """
        Proportional selection. Choose the parents with a probability proportional to each entity fitness
        :return: a list with selected parents
        """
        total_fitness = sum([x.distance for x in self.population])
        probs = [x.distance/total_fitness for x in self.population]
        # select half population to be parents with probability distribution probs
        parents = np.random.choice(self.population, int(self.population_number/2), replace=False, p=probs)
        return parents

    def select_survivors(self):
        self.population.sort(key=lambda x: x.distance)  # increase sort the population by fitness
        survivors = self.population[:self.population_number]  # take the best ones to form the population for next generation
        self.population = survivors

    def swap_mutation(self, entity):
        """
        Performs a mutation on an entity from population by swapping two cities
        :param entity: the entity from population
        :return: the mutated entity
        """
        return entity.swap_2_cities()

    def scramble_mutation(self, entity):
        """
        Randomly selects a sub route from the entity and shuffles the elements
        :param entity: the entity from population
        :return: the mutated entity
        """
        new_cities = entity.cities
        index1 = random.randrange(5, self.dimension-5)
        index2 = random.randrange(5, self.dimension-5)
        indices = [index1, index2]
        indices.sort()
        selected_sub_route = new_cities[indices[0]:indices[1]]
        random.shuffle(selected_sub_route)
        new_cities[indices[0]:indices[1]] = selected_sub_route
        entity.cities = new_cities
        return entity

    def order_crossover(self, parent1, parent2):
        """
        Alege o subruta dintr-un parinte si pastreaza ordinea
        relativa a oraselor din celalalt parinte
        :param parent1: first parent
        :param parent2: second parent
        :return: two children
        """
        parent1_cities = parent1.cities
        parent2_cities = parent2.cities

        # randomly choose a sub route from one parent to keep in one child
        i = random.randrange(4, self.dimension - 4)
        j = random.randrange(4, self.dimension - 4)
        if i > j:
            temp = i
            i = j
            j = temp
        sub_route1 = parent1_cities[i:j]
        sub_route2 = parent2_cities[i:j]
        cities1 = sub_route1  # se copiaza partea [i,j] din primul parinte in primul descendent
        cities2 = sub_route2  # se copiaza partea [i,j] din al doilea parinte in al doilea descendent
        shifted_ordered_parent2 = parent2_cities[j:] + parent2_cities[:j]  # se stabileste ordinea in al doilea parinte incepand cu pozitia j (se roteste lista de orase cu dimensiune-j pozitii)
        remaining_cities_2 = [city for city in shifted_ordered_parent2 if city not in cities1]  # se scot orasele din al doilea parinte care apar deja in primul copil
        for elem in range(j, self.dimension):  # se adauga circular in primul copil orasele ramase in al doilea parinte
            cities1.append(remaining_cities_2.pop(0))
        for elem in range(0, i):
            cities1.insert(0, remaining_cities_2.pop())

        # acelasi lucru ca mai sus pentru al doilea copil
        shifted_ordered_parent1 = parent1_cities[j:] + parent1_cities[:j]
        remaining_cities_1 = [city for city in shifted_ordered_parent1 if city not in cities2]
        for elem in range(j, self.dimension):
            cities2.append(remaining_cities_1.pop(0))
        for elem in range(0, i):
            cities2.insert(0, remaining_cities_1.pop())

        child1 = Route(self.dimension, cities1)
        child2 = Route(self.dimension, cities2)
        return child1, child2

    def partially_mapped_crossover(self, parent1, parent2):
        parent1_cities = parent1.cities
        parent2_cities = parent2.cities

        # randomly choose a sub route from one parent to keep in one child
        i = random.randrange(4, self.dimension - 4)
        j = random.randrange(4, self.dimension - 4)
        if i > j:
            temp = i
            i = j
            j = temp

        sub_route1 = parent1_cities[i:j]
        sub_route2 = parent2_cities[i:j]
        cities1 = [0] * self.dimension
        cities2 = [0] * self.dimension
        cities1[i:j] = sub_route2  # se copiaza partea [i,j] din primul parinte in primul descendent
        cities2[i:j] = sub_route1  # se copiaza partea [i,j] din al doilea parinte in al doilea descendent
        mapping1 = {}
        mapping2 = {}
        for index, elem in enumerate(sub_route1):
            mapping1[elem] = sub_route2[index]  # mapping parent1 - parent2

        for index, elem in enumerate(sub_route2):
            mapping2[elem] = sub_route1[index]  # mapping parent2 - parent1

        # create first child
        for index, elem in enumerate(parent1_cities[:i]):
            if elem not in cities1:
                cities1[index] = elem
            else:
                cities1[index] = mapping2.get(elem)

        for index, elem in enumerate(parent1_cities[j:]):
            if elem not in cities1:
                cities1[index+j] = elem
            else:
                cities1[index+j] = mapping2.get(elem)

        # create second child
        for index, elem in enumerate(parent2_cities[:i]):
            if elem not in cities2:
                cities2[index] = elem
            else:
                cities2[index] = mapping1.get(elem)

        for index, elem in enumerate(parent2_cities[j:]):
            if elem not in cities2:
                cities2[index+j] = elem
            else:
                cities2[index+j] = mapping1.get(elem)

        print(cities1)
        print(cities2)
        print("------------------------------------------------------------------------------------------------")
        for elem in cities1:
            print(elem)
            print(elem, " +  ", elem.to_string())
        for elem in cities2:
            print(elem)
            print(elem, " +  ", elem.to_string())
        child1 = Route(self.dimension, cities1)
        child2 = Route(self.dimension, cities2)
        return child1, child2

    def generic_algorithm1(self):
        best_solutions = []
        t = 0
        self.set_initial_population()  # initiate population
        while t < self.generation_number:
            parents = self.select_parents()   # select the parent
            random.shuffle(parents)  # shuffle the parent
            # set parents and get children
            for i in range(0, len(parents)-1, 2):
                # crossover the parents
                child1, child2 = self.order_crossover(parents[i], parents[i+1])
                # apply mutation to children
                child1 = self.swap_mutation(child1)
                child2 = self.swap_mutation(child2)
                self.population.append(child1)
                self.population.append(child2)

            # find the best solution from current generation
            current_best_solution = min(self.population, key=lambda x: x.distance)
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
            parents = self.select_parents()  # select the parent
            random.shuffle(parents)  # shuffle the parent
            # set parents and get children
            for i in range(0, len(parents) - 1, 2):
                # crossover the parents
                child1, child2 = self.order_crossover(parents[i], parents[i + 1])
                # apply mutation to children
                child1 = self.scramble_mutation(child1)
                child2 = self.scramble_mutation(child2)
                self.population.append(child1)
                self.population.append(child2)

            # find the best solution from current generation
            current_best_solution = min(self.population, key=lambda x: x.distance)
            best_solutions.append(current_best_solution)

            # select the survivors for next generation
            self.select_survivors()

            t += 1

        return best_solutions
