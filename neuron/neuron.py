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

    def __init__(self):
        self.w1 = np.random.randn()
        self.w2 = np.random.randn()
        self.bias = np.random.randn()

    def viz():
        X = np.linspace(-1.05,1.05,100)
        Y = np.linspace(-1.05,1.05,100)
        output = np.zeros((100,100))

        i = 0
        for x in X:
            j = 0
            for y in Y:
                output[i,j] = a.forward(x,y)
                j += 1
            i += 1

        plt.pcolormesh(X,Y,output)
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.show()


    def forward(self, i1, i2):
        return step((self.w1 * i1) + (self.w2 * i2) + self.bias)