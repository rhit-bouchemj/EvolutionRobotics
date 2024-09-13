import numpy as np
import sys

class Agent():

    def __init__(self):
        self.xPos = 0
        self.yPos = 0
        self.direction = 0 #in radians (0 - 2pi)
        self.velocity = 1
        self.sourceDistance = 1.0
        # self.prevSourceDistance = sys.maxint

    def calculateSourceDistance(self, sourceX, sourceY):
        sourceDistance = np.sqrt(((self.xPos - sourceX) ** 2) + ((self.yPos-sourceY) ** 2))
        return sourceDistance
    
    # def movedFarther(self):
    #     return self.sourceDistance > self.prevSourceDistance

    def getSourceDistance(self):
        return self.sourceDistance

    def getX(self):
        return self.xPos

    def getY(self):
        return self.yPos
    
    def rotate(self):
        self.direction = np.random.random() * 2 * np.pi

    def move(self):
        self.velocity = np.random.random() * 0.5
        self.xPos += self.velocity * np.cos(self.direction)
        self.yPos += self.velocity * np.sin(self.direction)

    def step(self):
        self.rotate()
        self.move()

    def getOriginDistance(self):
        originDistance = np.sqrt((self.xPos ** 2) + (self.yPos ** 2))
        return originDistance