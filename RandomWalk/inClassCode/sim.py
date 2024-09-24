import agent
import matplotlib.pyplot as plt
import numpy as np

def runIndSim(duration):
    walker = agent.Agent()
    xlist = np.zeros(duration+1)
    ylist = np.zeros(duration+1)
    for i in range(duration):
        walker.step()
        xlist[i+1] = walker.x
        ylist[i+1] = walker.y
    return xlist, ylist

x,y = runIndSim(100000)
plt.plot(x,y)
plt.plot(0,0,'ro')
plt.plot(x[-1],y[-1],'ko')
plt.xlabel("x")
plt.ylabel("y")
plt.show()

def runGroup(popsize, duration):
    xlist = np.zeros((popsize,duration+1))
    ylist = np.zeros((popsize,duration+1))
    for i in range(popsize):
        xlist[i], ylist[i] = runIndSim(duration)
    return xlist,ylist

x,y = runGroup(100, 10000)
plt.plot(x.T,y.T)
plt.plot(0,0,'ro')
plt.plot(x.T[-1],y.T[-1],'ko')
plt.xlabel("x")
plt.ylabel("y")
plt.show()

def runIndSimX(duration):
    walker = agent.Agent()
    dlist = np.zeros(duration+1)
    for i in range(duration):
        walker.step()
        dlist[i+1] = walker.dist()
    return dlist

def runGroupX(popsize, duration):
    dlist = np.zeros((popsize,duration+1))
    for i in range(popsize):
        dlist[i] = runIndSimX(duration)
    return dlist

d = runGroupX(100, 10000)
plt.plot(d.T)
plt.plot(np.mean(d,0),'k')
plt.xlabel("Time")
plt.ylabel("Distance to the start")
plt.show()

