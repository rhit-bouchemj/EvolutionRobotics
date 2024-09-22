import numpy as np

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

    def forward(self, int1, int2):
        return step((self.w1 * int1) + (self.w2 * int2) + (self.bias))