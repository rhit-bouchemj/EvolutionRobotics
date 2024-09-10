import numpy as np

class Agent():

    def __init__(self):
        self.xPos = 0
        self.yPos = 0
        self.direction = 0 #in radians (0 - 2pi)

    def getX(self):
        return self.xPos

    def getY(self):
        return self.yPos
    
    def rotate(self):
        self.direction = np.random.random() * 2 * np.pi

    def move(self):
        stepMagnitude = np.random.random()
        self.xPos += stepMagnitude * np.cos(self.direction)
        self.yPos += stepMagnitude * np.sin(self.direction)

    def step(self):
        self.rotate()
        self.move()
