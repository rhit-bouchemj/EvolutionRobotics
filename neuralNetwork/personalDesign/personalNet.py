# Class to take in a neural network

import numpy as np
import ea

class eaNeuralNet():
    def __init__(self, unitsPerLayer):
        self.unitsPerLayer = unitsPerLayer
        self.numLayers = len(unitsPerLayer)
        self.weights = []
        self.biases = []
    
    def setWeights(self, inputWeights):
        i = 0
        for layer in range(self.numLayers):
            currentWeights = []
            for unit in range(self.unitsPerLayer[layer]):
                currentWeights.append(inputWeights[i])
                i += 1
            self.weights.append(currentWeights)
        
    def setBiases(self, inputBias):
        i = 0
        for layer in range(self.numLayers):
            currentWeights = []
            for unit in range(self.unitsPerLayer[layer]):
                currentWeights.append(inputBias[i])
                i += 1
            self.weights.append(currentWeights)