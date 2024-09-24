import numpy as np
import matplotlib.pyplot as plt

def step(x):
    if x <= 0:
        return 0
    else: 
        return 1

def sigmoid(x):
    return 1/(1+np.exp(-x))
    
class Perceptron:

    def __init__(self, inputs, lr):
        self.W = np.random.randn(inputs)
        self.bias = np.random.randn()
        self.lr = lr
    
    def forward(self, I):
        return sigmoid(np.dot(self.W,I) + self.bias)
    
    def train(self, I, target):
        output = self.forward(I)
        error = target - output
        self.W += error * I * self.lr
        self.bias += error * self.lr
        return abs(error)

    def viz(self, granular, title):
        X = np.linspace(-1.05,1.05,granular)
        Y = np.linspace(-1.05,1.05,granular)
        output = np.zeros((granular,granular))
        i = 0
        for x in X:
            j = 0
            for y in Y:
                output[i,j] = self.forward([x,y])
                j += 1
            i += 1

        plt.pcolormesh(X,Y,output)
        plt.colorbar()
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.title(title)
        plt.show()
