import agent
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np



def main():
        loopIterations = 100
        (xPosList, yPosList) = singleOrganismSimulation(loopIterations)
        print(xPosList)
        print(yPosList)
        animateGraph(loopIterations, xPosList, yPosList)
        # line, = ax.plot([],[], '-')
    
        
def singleOrganismSimulation(iterations):
    loopIterations = iterations
    organism = agent.Agent()
    xPosList = np.zeros(iterations)
    yPosList = np.zeros(iterations)
    for i in range(1,iterations):
        organism.step()
        xPosList[i] = organism.getX()
        yPosList[i] = organism.getY()

    # graphPlot(xPosList, yPosList)
    return xPosList, yPosList



def graphPlot(xPositions, yPositions):
     plt.plot(xPositions, yPositions)
     plt.plot(0,0, 'ro')
     plt.plot(xPositions[-1], yPositions[-1], 'ko')
     plt.show()

def animate(i, xList, yList):
    
    ax.plot(xList[:i], yList[:i])
    # x_data.append(i)
    # y_data.append(np.sin(i))
    # line.set_data(x_data, y_data)

    line.set_data(xList[:i], yList[:i])
    return line,
    # ax.set_xlim([-10,10])
    # ax.set_ylim([-10,10])





# def animateGraph(iterations, xList, yList):
    # ani = animation.FuncAnimation(fig, animate, frames=np.linspace(0, 10, 100), init_func=graphInit, blit=True)

# def graphInit():
#     ax.set_xlim(-5, 5)
#     ax.set_ylim(-5, 5)
#     return line,

def animate(i, xList, yList, axel, line):
    # axel.plot(xList[:i], yList[:i])
    line.set_data(xList[:i], yList[:i])
    return line,

def animateGraph(iterations, xList, yList):

    fig, ax = plt.subplots()
    line, = plt.plot([],[], 'b-', animated=True)
    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 5)

    def animate(i, xList, yList):
        line.set_data(xList[:i], yList[:i])
        return line,

    ani = animation.FuncAnimation(fig, animate, frames=iterations, fargs=(xList, yList, ), interval=100, repeat=False)
    # plt.plot(0, 0, 'ro')
    plt.show()
    # recordGraph = animation.FuncAnimation(liveMap, )
        


# ax.set_xlim(-10, 10)
# ax.set_ylim(-10, 10)
main()
# plt.show()

