import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import agent



def main():
        loopIterations = 1000
        pop = 50
        sensing = False

        #Create a stimulus source at X,Y
        source = [80, -20]

        (xPosList, yPosList, distanceList) = multipleOrganismSimulation(pop, loopIterations, sensing, source)
        
        plotDistance(loopIterations, distanceList, pop)
        animate_plot(loopIterations, xPosList, yPosList, pop)
    
        
def singleOrganismSimulation(iterations, sensing, source):
    loopIterations = iterations
    organism = agent.Agent()
    if(sensing):
        organism.setSensing()
    xPosList = np.zeros(iterations)
    yPosList = np.zeros(iterations)
    distance = np.zeros(iterations)
    for i in range(1,iterations):
        organism.calculateSourceDistance(source[0], source[1])
        organism.step()
        xPosList[i] = organism.getX()
        yPosList[i] = organism.getY()
        distance[i] = organism.getOriginDistance()
    return xPosList, yPosList, distance


def multipleOrganismSimulation(population, iterations, sensing=False, source=[0,0]):
    xPosList = np.zeros((population, iterations))
    yPosList = np.zeros((population, iterations))
    distance = np.zeros((population, iterations))
    for numOrganism in range(population):
        currentXList, currentYList, currentDistance = singleOrganismSimulation(iterations, sensing, source)
        xPosList[numOrganism] = currentXList
        yPosList[numOrganism] = currentYList
        distance[numOrganism] = currentDistance
    return xPosList, yPosList, distance

def animate_plot(iteration, xList, yList, population=1, frameModifer=3):
    fig1, ax1 = plt.subplots()
    x_data = [[] for numLine in range(population)]
    y_data = [[] for numLine in range(population)]
    lines = [ax1.plot([], [], animated=True)[0] for lineNum in range(population)]
    origin_dot, = plt.plot(0, 0, 'ko', markersize=3)  # 'ko' means black color ('k') and circle marker ('o')
    end_dots, = plt.plot(xList.T[-1], yList.T[-1], 'ko', marker='2')

    # colors = plt.cm.viridis(np.linspace(0, 1, population))  # Generate a range of colors for lines
    colors = plt.cm.hsv(np.linspace(0, 1, population))  # 'hsv' covers the full spectrum of hues

    for line, color in zip(lines, colors):
        line.set_color(color)

    def init():
        xLim = 100
        yLim = 50
        ax1.set_xlim(-xLim, xLim)
        ax1.set_ylim(-yLim, yLim)
        return lines + [origin_dot] + [end_dots]
    
    def update(frame, xList, yList, frameModifer):
        for numLine in range(population):
            x_data[numLine] = (xList[numLine][:frame*frameModifer])
            y_data[numLine] = (yList[numLine][:frame*frameModifer])
            lines[numLine].set_data(x_data[numLine], y_data[numLine])
        return lines + [origin_dot] + [end_dots]

    ani = FuncAnimation(fig1, update, fargs=(xList, yList, frameModifer, ), frames=iteration+1, interval=1, init_func=init, blit=True, repeat=False)
    # plt.plot( 0,0,'ko')
    plt.show()  # Display the plot

def plotDistance(iterations, distances, population):
    fig2, ax2 = plt.subplots()
    ax2.set_xlabel("Step Number")
    ax2.set_ylabel("Distane from Origin")
    stepNum = range(0, iterations)
    colors = plt.cm.hsv(np.linspace(0, 1, population))  # 'hsv' covers the full spectrum of hues
    avgDistance = np.zeros(iterations)
    for i in range(iterations):
        avgDistance[i] = np.average(distances.T[i])
    for i in range(population):
        ax2.plot(stepNum, distances[i], color=colors[i], label=f'Line {i+1}')  # Assigning different colors and labels
    ax2.plot(stepNum, avgDistance, 'k')

main()
