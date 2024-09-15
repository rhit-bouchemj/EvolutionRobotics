import numpy as np
import sys

class Agent():

    def __init__(self):
        self.xPos = 0
        self.yPos = 0
        self.direction = 0 #in radians (0 - 2pi)
        self.velocity = 0.5
        self.sourceDistance = 1.0
        self.prevSourceDistance = 0.0 #sys.maxsize
        self.probabilityToRotate = 0.5
        self.sensing = False

    def setSensing(self):
        self.sensing = True

    def calculateSourceDistance(self, sourceX, sourceY):
        self.sourceDistance = np.sqrt(((self.xPos - sourceX) ** 2) + ((self.yPos-sourceY) ** 2))
        return self.sourceDistance
    
    # def checkMovedFarther(self):
    #     self.movedFarther = self.sourceDistance > self.prevSourceDistance
    def movedFarther(self):
        return self.sourceDistance > self.prevSourceDistance
        
    def getSourceDistance(self):
        return self.sourceDistance

    def getX(self):
        return self.xPos

    def getY(self):
        return self.yPos
    
    def rotate(self):
        self.direction = np.random.random() * 2 * np.pi

    def move(self):
        # self.velocity = np.random.random() * 0.5
        self.xPos += self.velocity * np.cos(self.direction)
        self.yPos += self.velocity * np.sin(self.direction)

    def step(self):
        # if(np.random.random() = self.probabilityToRotate):
        if(self.sensing):
            # self.checkMovedFarther()
            if(self.movedFarther() or (np.random.random() < self.probabilityToRotate)): #add random noise
                self.rotate()
            # else:
                # print("notTurn")
            self.prevSourceDistance = self.sourceDistance
        else:
            self.rotate()
        self.move()

    def getOriginDistance(self):
        originDistance = np.sqrt((self.xPos ** 2) + (self.yPos ** 2))
        return originDistance