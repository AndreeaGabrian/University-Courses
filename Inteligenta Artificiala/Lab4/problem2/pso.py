import random
import numpy as np

from problem2.Particle import Particle
from problem2.Particle import fitness


class PSO:
    def __init__(self, population_number, iteration_number, bounds, dimension):
        self.population_number = population_number
        self.iteration_number = iteration_number
        self.population = []  # list of Solution objects
        self.bounds = bounds  # list with lower and upper bound for function domain
        self.dimension = dimension

    def set_initial_population(self):
        """
        Generates random solutions for initial population of particles with 0 velocity and pbest as initial fitness
        :return: the initial population
        """
        for i in range(self.population_number):
            point = np.random.uniform(low=self.bounds[0], high=self.bounds[1], size=self.dimension)
            self.population.append(Particle(point, [0]*self.dimension))


    def pso_alg(self, c1, c2, w, vmax):
        """

        :param c1:
        :param c2:
        :param w:
        :return:
        """
        # set population, velocities and pbest
        self.set_initial_population()
        population = self.population
        gbests = []
        # set initial global best
        gbest_particle = min(population, key=lambda x: x.fitness)
        gbests.append(gbest_particle)

        for i in range(self.iteration_number):

            # gbests.append(gbest_particle)

            # update velocities and positions
            for x in population:
                # update velocity
                new_velocity = w * np.array(x.velocity) + c1 * random.uniform(0, 1) * (np.array(x.pbest_position) - np.array(x.position)) + c2 * random.uniform(0, 1) * (np.array(gbest_particle.position) - np.array(x.position))

                # limit the velocity
                for i, val in enumerate(new_velocity):
                    if val > vmax:
                        new_velocity[i] = val

                # set new velocity
                x.velocity = new_velocity

                # update position
                x.position = x.position + new_velocity

                # after updating the position if it is out of bound set it to bounds
                for i, elem in enumerate(x.position):
                    if elem < self.bounds[0]:
                        x.position[i] = self.bounds[0]
                    if elem > self.bounds[1]:
                        x.position[i] = self.bounds[1]

                # calculate new fitness
                current_fitness = fitness(x.position)
                x.fitness = current_fitness

                # calculate pbest and update if necessary
                if current_fitness < x.pbest_fitness:
                    x.pbest_fitness = current_fitness
                    x.pbest_position = x.position

            # update gbest
            for x in population:
                if x.pbest_fitness < gbest_particle.pbest_fitness:
                    gbest_particle = x
                    gbests.append(gbest_particle)

            w -= 0.001  # Reduce inertia weight over time

        return gbests










