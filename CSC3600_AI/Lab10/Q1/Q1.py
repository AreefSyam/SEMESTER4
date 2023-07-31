import random
import string

# Target string
target_string = "Genetic Algorithm: Nature-inspired Optimization Technique"

# Constants
GENES = string.ascii_letters + string.digits + string.punctuation + " "
POPULATION_SIZE = 100
MUTATION_RATE = 0.01

class Individual:
    def __init__(self, chromosome):
        self.chromosome = chromosome
        self.fitness = self.calculate_fitness()

    def calculate_fitness(self):
        # Calculate the fitness value of an individual by comparing its chromosome with the target string
        fitness = 0
        for i in range(len(target_string)):
            if self.chromosome[i] != target_string[i]:
                fitness += 1
        return fitness

    def mate(self, partner):
        # Perform mating between two individuals to create a new individual
        child_chromosome = ""
        for i in range(len(self.chromosome)):
            # Randomly select genes from the parents' chromosomes
            if random.random() < 0.5:
                child_chromosome += self.chromosome[i]
            else:
                child_chromosome += partner.chromosome[i]
        return Individual(child_chromosome)

    def mutate(self):
        # Introduce random mutations in an individual's chromosome
        mutated_chromosome = ""
        for gene in self.chromosome:
            if random.random() < MUTATION_RATE:
                # Randomly replace genes with other genes from the GENES set
                mutated_chromosome += random.choice(GENES)
            else:
                mutated_chromosome += gene
        return Individual(mutated_chromosome)

def generate_initial_population():
    # Generate an initial population of individuals with random chromosomes
    population = []
    for _ in range(POPULATION_SIZE):
        chromosome = ''.join(random.choice(GENES) for _ in range(len(target_string)))
        population.append(Individual(chromosome))
    return population

def evolve_population(population):
    # Evolve the population by selecting parents, generating offspring through mating and mutation
    new_population = []
    population.sort(key=lambda x: x.fitness)
    for i in range(int(POPULATION_SIZE / 2)):
        parent1 = population[i]
        parent2 = population[i + 1]
        offspring = parent1.mate(parent2)
        new_population.append(offspring)
        mutated_offspring = offspring.mutate()
        new_population.append(mutated_offspring)
    return new_population

def genetic_algorithm():
    # Main driver function to run the genetic algorithm
    population = generate_initial_population()
    generation = 1
    while True:
        population = evolve_population(population)
        best_individual = population[0]
        print(f"Generation: {generation}\tBest Fitness: {best_individual.fitness}\tChromosome: {best_individual.chromosome}")
        if best_individual.fitness == 0:
            break
        generation += 1
    print("Genetic Algorithm finished.")

# Run the algorithm
genetic_algorithm()
