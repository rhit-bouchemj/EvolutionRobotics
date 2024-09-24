import numpy as np

class Agent():

    def __init__(self):
        self.x = 0
        self.y = 0
        self.orientation = np.random.random() * 2 * np.pi
        self.vel = 1

    def step(self):
        self.orientation += np.random.normal()*np.pi/8 #np.random.random() * 2 * np.pi
        self.x += self.vel * np.cos(self.orientation)
        self.y += self.vel * np.sin(self.orientation)

    def dist(self):
        return np.sqrt(self.x**2 + self.y**2)
