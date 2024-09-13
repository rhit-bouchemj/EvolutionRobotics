import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import agent



def main():
        loopIterations = 1000
        pop = 60

        #Create a stimulus source at 
        sourceX = 30
        sourceY = 20

        (xPosList, yPosList) = multipleOrganismSimulation(pop, loopIterations)
        print(xPosList)
        print(yPosList)
        animate_plot(loopIterations, xPosList, yPosList, pop)
    
        
def singleOrganismSimulation(iterations):
    loopIterations = iterations
    organism = agent.Agent()
    xPosList = np.zeros(iterations)
    yPosList = np.zeros(iterations)
    for i in range(1,iterations):
        organism.step()
        xPosList[i] = organism.getX()
        yPosList[i] = organism.getY()
    return xPosList, yPosList


def multipleOrganismSimulation(population, iterations):
    xPosList = np.zeros((population, iterations))
    yPosList = np.zeros((population, iterations))
    for numOrganism in range(population):
        currentXList, currentYList = singleOrganismSimulation(iterations)
        xPosList[numOrganism] = currentXList
        yPosList[numOrganism] = currentYList
    return xPosList, yPosList

def animate_plot(iteration, xList, yList, population=1):
    fig, ax = plt.subplots()
    x_data = [[] for numLine in range(population)]
    y_data = [[] for numLine in range(population)]
    lines = [ax.plot([], [], animated=True)[0] for lineNum in range(population)]
    origin_dot, = plt.plot(0, 0, 'ko', markersize=3)  # 'ko' means black color ('k') and circle marker ('o')
    end_dots, = plt.plot(xList.T[-1], yList.T[-1], 'mo', marker='2')

    # colors = plt.cm.viridis(np.linspace(0, 1, population))  # Generate a range of colors for lines
    colors = plt.cm.hsv(np.linspace(0, 1, population))  # 'hsv' covers the full spectrum of hues

    for line, color in zip(lines, colors):
        line.set_color(color)

    def init():
        ax.set_xlim(-50, 50)
        ax.set_ylim(-50, 50)
        return lines + [origin_dot] + [end_dots]
    
    def update(frame, xList, yList):
        for numLine in range(population):
            x_data[numLine].append(xList[numLine][frame])
            y_data[numLine].append(yList[numLine][frame])
            lines[numLine].set_data(x_data[numLine], y_data[numLine])
        return lines + [origin_dot] + [end_dots]

    ani = FuncAnimation(fig, update, fargs=(xList, yList, ), frames=iteration, interval=1, init_func=init, blit=True, repeat=False)
    # plt.plot( 0,0,'ko')
    plt.show()  # Display the plot

main()
