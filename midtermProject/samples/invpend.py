import numpy as np

def angle_normalize(x): # input = radians
    return (((x+np.pi) % (2*np.pi)) - np.pi) #put range of angle to -pi to pi (0 = hanging down)

class InvPendulum(): # TODO: change so that gravity acts on the center of mass of pendulum?

    def __init__(self):
        self.max_speed = 8.0    # TODO: rotational speed?
        self.max_torque = 2.0   # Max instant force?
        self.g = 10.0           # gravity
        self.m = 1.0            # mass
        self.l = 1.0            # pole length
        self.theta = 0.0        # angle of pendulum
        self.theta_dot = 0.0    # rate of change of pendulum angle
        self.force_mag = 2.0    #magnitude of force

    def step(self, stepsize, u): # stepsize = amt of steps in a "second" (what should be set time), u = ? (array)
        u = np.clip(u*self.force_mag, -self.max_torque, self.max_torque)[0] # u = force?
        cost = angle_normalize(self.theta)**2 + .1*self.theta_dot**2 + .001*(u**2)
        self.theta_dot += stepsize * (-3*self.g/(2*self.l) * np.sin(self.theta + np.pi) + 3./(self.m*self.l**2)*u)
        self.theta += stepsize * self.theta_dot
        self.theta_dot = np.clip(self.theta_dot, -self.max_speed, self.max_speed)
        return -cost*stepsize

    def state(self):
        return np.array([np.cos(self.theta), np.sin(self.theta), self.theta_dot]) #state of system defined  by cos, sin, and RoC of angle (need cos and sin?)
