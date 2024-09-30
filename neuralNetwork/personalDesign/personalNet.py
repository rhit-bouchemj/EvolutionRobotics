import random
import numpy as np

class EvolutionaryNeuralNet:
    def __init__(self, hiddenLayers, hiddenUnits, r):
        self.nl = hiddenLayers
        self.nh = hiddenUnits
        self.range = r

    def create_network(self):
        # Create a new network with random weights
        network = []
        for l in range(self.nl):
            layer = []
            for _ in range(self.nh):
                if l == 0:
                    layer.append(Perceptron(2, 0.1, self.range))  # First hidden layer
                else:
                    layer.append(Perceptron(self.nh, 0.1, self.range))  # Subsequent hidden layers
            network.append(layer)
        output_layer = Perceptron(self.nh, 0.1, self.range)  # Output layer
        return network, output_layer

    def forward(self, network, output_layer, Input):
        # Forward pass through the network
        for layer in network:
            layer_output = []
            for unit in layer:
                layer_output.append(unit.forward(Input))
            Input = layer_output
        return output_layer.forward(Input)

    def evaluate_fitness(self, network, output_layer, data, labels):
        # Calculate fitness as the inverse of the total error (or accuracy)
        fitness = 0
        for i, sample in enumerate(data):
            output = self.forward(network, output_layer, sample)
            fitness += 1 - abs(output - labels[i])  # Fitness based on accuracy
        return fitness

    def crossover(self, parent1, parent2):
        # Perform crossover between two networks (weight blending)
        child_network = []
        for l in range(len(parent1[0])):  # Iterate over layers
            child_layer = []
            for i in range(len(parent1[0][l])):  # Iterate over perceptrons in the layer
                child_perceptron = Perceptron(2 if l == 0 else self.nh, 0.1, self.range)
                child_perceptron.W = np.where(np.random.rand(len(parent1[0][l][i].W)) < 0.5,
                                              parent1[0][l][i].W, parent2[0][l][i].W)  # Crossover for weights
                child_layer.append(child_perceptron)
            child_network.append(child_layer)

        # Crossover the output layer
        child_output_layer = Perceptron(self.nh, 0.1, self.range)
        child_output_layer.W = np.where(np.random.rand(len(parent1[1].W)) < 0.5,
                                        parent1[1].W, parent2[1].W)  # Crossover for output layer weights
        return child_network, child_output_layer

    def mutate(self, network, output_layer, mutation_rate=0.01):
        # Mutate network weights by adding small random changes
        for layer in network:
            for unit in layer:
                unit.W += np.random.randn(len(unit.W)) * mutation_rate  # Add random noise to weights
                unit.bias += np.random.randn() * mutation_rate

        output_layer.W += np.random.randn(len(output_layer.W)) * mutation_rate  # Mutate output layer weights
        output_layer.bias += np.random.randn() * mutation_rate

    def evolve(self, data, labels, generations=100, population_size=20, mutation_rate=0.01):
        # Initialize a population of neural networks
        population = [(self.create_network(), 0) for _ in range(population_size)]  # (network, fitness)
        
        for gen in range(generations):
            # Evaluate fitness of each network
            for i in range(population_size):
                network, output_layer = population[i][0]
                fitness = self.evaluate_fitness(network, output_layer, data, labels)
                population[i] = (population[i][0], fitness)
            
            # Sort population by fitness (higher is better)
            population = sorted(population, key=lambda x: x[1], reverse=True)
            print(f"Generation {gen}, Best fitness: {population[0][1]}")
            
            # Select the top-performing networks (elitism)
            next_population = population[:population_size // 2]
            
            # Generate the next generation through crossover and mutation
            while len(next_population) < population_size:
                parent1 = random.choice(population[:population_size // 2])[0]
                parent2 = random.choice(population[:population_size // 2])[0]
                child = self.crossover(parent1, parent2)
                self.mutate(child[0], child[1], mutation_rate)
                next_population.append((child, 0))  # New child with fitness = 0

            population = next_population  # Replace old population with the new one
            
        # Return the best network after evolution
        return population[0][0], population[0][1]  # Best network and fitness
