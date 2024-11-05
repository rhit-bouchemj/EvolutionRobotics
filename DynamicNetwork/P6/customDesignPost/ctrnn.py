import numpy as np

def sigmoid(x):
    return 1/(1+np.exp(-x))

class CTRNN():

    def __init__(self, size):
        self.Size = size                        # number of neurons in the circuit
        self.States = np.zeros(size)            # state of the neurons
        self.TimeConstants = np.ones(size)      # time-constant for each neuron
        self.invTimeConstants = 1.0/self.TimeConstants
        self.Biases = np.zeros(size)            # bias for each neuron
        self.Weights = np.zeros((size,size))    # connection weight for each pair of neurons (2D array [each neuron is weighted by all other neurons])
        self.Outputs = np.zeros(size)           # neuron outputs
        self.Inputs = np.zeros(size)            # external input to each neuron

    def setParameters(self, weights, biases, timeconstants): #set values
        self.Weights =  np.array(weights)
        self.Biases =  np.array(biases)
        self.TimeConstants =  np.array(timeconstants)
        self.invTimeConstants = 1.0/self.TimeConstants        

    def randomizeParameters(self, diff=10, tDiff=5.0): #randomize values between -10 to 10 and 0.1-5 for params
        self.Weights = np.random.uniform(-diff,diff,size=(self.Size,self.Size))
        self.Biases = np.random.uniform(-diff,diff,size=(self.Size))
        self.TimeConstants = np.random.uniform(0.1,tDiff,size=(self.Size))
        self.invTimeConstants = 1.0/self.TimeConstants

    def initializeState(self, s):
        self.Inputs = np.zeros(self.Size)   #input starts as nothing
        self.States = s
        self.Outputs = sigmoid(self.States+self.Biases)     #output when starting at nothing

    def step(self, dt):
        # print(self.Inputs, np.dot(self.Weights.T, self.Outputs))
        netinput = self.Inputs + np.dot(self.Weights.T, self.Outputs)       #input into next state?
        self.States += dt * (self.invTimeConstants*(-self.States+netinput)) #y* = 1/T * (-y + sum + I)
        self.Outputs = sigmoid(self.States+self.Biases) #where add external input?

    def save(self, filename):
        np.savez(filename, size=self.Size, weights=self.Weights, biases=self.Biases, timeconstants=self.TimeConstants) # safe parameters? should theoretically recalculate same values

    def load(self, filename):
        params = np.load(filename)      #load saved file for parameters
        self.Size = params['size']
        self.Weights = params['weights']
        self.Biases = params['biases']
        self.TimeConstants = params['timeconstants']
        self.invTimeConstants = 1.0/self.TimeConstants

    def shiftedOutput(self, shiftValue):
        return 2*np.pi*self.Outputs - np.pi