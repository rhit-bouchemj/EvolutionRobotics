import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import agent



def main():
        loopIterations = 100
        pop = 2
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
    xPosList = np.zeros((population, iterations-1))
    yPosList = np.zeros((population, iterations-1))
    for numOrganism in range(population):
        currentXList, currentYList = singleOrganismSimulation(iterations)
        xPosList[numOrganism] = currentXList
        yPosList[numOrganism] = currentYList
    return xPosList, yPosList




def animate_plot(iteration, xList, yList, population=1):
    # Create a figure and an axes
    fig, ax = plt.subplots()
    x_data, y_data = [], []
    ln, = plt.plot([], [], 'b-', animated=True)
    ln2, = ax.plot([],[],'ro')

    # Initialize the plot limits
    def init():
        # plt.clf()
        ax.set_xlim(-10, 10)
        ax.set_ylim(-10, 10)
        return ln,

    # Update the plot with new data points to extend the line
    def update(frame, xList, yList):
        x_data.append(xList[frame])
        y_data.append(yList[frame])
        ln.set_data(x_data, y_data)
        ln2.set_data(np.zeros(1), np.zeros(1))
        return (ln, ln2)

    # Create an animation object
    ani = FuncAnimation(fig, update, fargs=(xList, yList, ), frames=iteration, interval=100, init_func=init, blit=True, repeat=False)
    plt.show()  # Display the plot

# Call the function to animate and display the plot
main()
