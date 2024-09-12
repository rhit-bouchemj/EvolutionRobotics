import numpy as np

class Agent():

    def __init__(self):
        self.xPos = 0
        self.yPos = 0
        self.direction = 0 #in radians (0 - 2pi)
        self.velocity = 1

    def getX(self):
        return self.xPos

    def getY(self):
        return self.yPos
    
    def rotate(self):
        self.direction = np.random.random() * 2 * np.pi

    def move(self):
        self.velocity = np.random.random()
        self.xPos += self.velocity * np.cos(self.direction)
        self.yPos += self.velocity * np.sin(self.direction)

    def step(self):
        self.rotate()
        self.move()

    def getDistance(self):
        distance = np.sqrt((self.xPos ** 2) + (self.yPos ** 2))
        return distance