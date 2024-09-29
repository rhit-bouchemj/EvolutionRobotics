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

    def __init__(self, inputs, lr, range):
        self.W = np.random.random(inputs)*2*range - range #Weights <-- between -range and range
        self.bias = np.random.random()*2*range - range # bias value <-- between -range and range
        self.lr = lr # Learning Rate
    
    def forward(self, I):
        return sigmoid(np.dot(self.W,I) + self.bias) #forward is a sigmoid function (weight*in + bias)
    
    def train(self, I, target):
        output = self.forward(I) # output = function
        error = target - output # error = desired value - output
        self.W += error * I * self.lr # adjust weight based on the error value, input, and learning rate
        self.bias += error * self.lr # adjust bias based on error and learning rate
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


class NeuralNet():

    def __init__(self,hiddenUnits,r): #r = range
        self.nh = hiddenUnits # number of layers?
        self.H = [] # array of perceptrons
        for i in range(self.nh): # add # of hiddenlayers as perceptrons
            self.H.append(Perceptron(2,0.1,r)) # each perceptron has 2 inputs and a learning rate of 0.1
        self.nO = Perceptron(hiddenUnits,0.1,r) # final output of network

    def forward(self,Input):
        hiddenOutput = []
        for unit in self.H:
            hiddenOutput.append(unit.forward(Input)) # Get array of all hidden layer's output
        return self.nO.forward(hiddenOutput) # final output = based on list of inputs (which is outputs of hidden layers)

    def train(self,Input,target):
        # 3. Propagate forward
        hiddenOutput = []
        for unit in self.H:
            hiddenOutput.append(unit.forward(Input))
        output = self.nO.forward(hiddenOutput) # could have just called "forward" method

        # 4. Calculate error for the output neuron
        derivative = output * (1.0 - output) # derivative = normalized to 0.25 max
        errorOutput = (target - output)*derivative #error = difference * derivative (normalize?)

        # 5. Calculate error for the hidden units
        error = []
        for i in range(self.nh):
            derivative = hiddenOutput[i] * (1.0 - hiddenOutput[i])
            error.append(self.nO.W[i] * errorOutput * derivative) # use self.nO.W because it holds the weights of the hidden layer

        # Update the hidden-output weights
        for i in range(self.nh):
            self.nO.W[i] += hiddenOutput[i] * errorOutput * 0.1 #assumes learning rate = 0.1 always
        self.nO.bias += errorOutput * 0.1

        # Update the input-hidden weights
        for i in range(self.nh):
            self.H[i].W[0] += Input[0] * error[i] * 0.1
            self.H[i].W[1] += Input[1] * error[i] * 0.1
            self.H[i].bias += 1 * error[i] * 0.1

        return abs(errorOutput)
    
    def viz2(self, granular, title, dataset, label):
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

        for i in range(len(dataset)):
            if label[i] == 1:
                plt.plot(dataset[i][0],dataset[i][1],'wo')
            else:
                plt.plot(dataset[i][0],dataset[i][1],'wx')

        plt.title(title)
        plt.show()

    